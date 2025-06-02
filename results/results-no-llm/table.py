import re
import pandas as pd

# Load the CSV file
df = pd.read_csv('results-no-llm.csv')

def extract_project(filename):
    match = re.search(r"results-(.*?)(_no_llm|-no_llm)", filename)
    name = match.group(1) if match else "Unknown"
    return "MODIS" if name == "ModisDataset" else name[0].upper() + name[1:]

def extract_topK(filename):
    #results-CM1-NASA_no_llm-1.json_c399af43-7604-3608-9acb-49f6058b63e4.md
    match = re.search(r".*_no_llm-(.*?).json", filename)
    topK = match.group(1) if match else "Unknown"
    if match == "Unknown":
        print(f"[WARN] Could not extract TopK from filename: {filename}")
        exit(1)
    return topK

df['ProjectName'] = df['File'].apply(extract_project)
df['TopK'] = df['File'].apply(extract_topK)
df['Approach'] = 'Embeddings'

# Ensure correct data types
df['TopK'] = pd.to_numeric(df['TopK'], errors='coerce')
df['Precision'] = pd.to_numeric(df['Precision'], errors='coerce')
df['Recall'] = pd.to_numeric(df['Recall'], errors='coerce')
df['F2'] = 5 * (df['Precision'] * df['Recall']) / (4 * df['Precision'] + df['Recall'])

# Sort for consistency
df = df.sort_values(by='TopK')

# (1) Best topK per project (max F2 per project-approach)
best_per_project = df.loc[df.groupby(['ProjectName', 'Approach'])['F2'].idxmax()]

# (2) Compute average F2 per approach-topK pair
avg_f2_per_topK = df.groupby(['Approach', 'TopK'])['F2'].mean().reset_index()

# (3) For each approach, find the topK with the highest average F2
best_avg_topK = avg_f2_per_topK.loc[avg_f2_per_topK.groupby('Approach')['F2'].idxmax()]
best_avg_topK.columns = ['Approach', 'Best_TopK', 'Average_Best_F2']

# Output summary
print("\n=== Best TopK per Approach Based on Highest Average F2 Across Projects ===")
print(best_avg_topK)

# (4) Output best topKs per project (as originally computed)
print("\n=== Best TopK per Project and Approach (Based on Max F2) ===")
print(best_per_project[['Approach', 'ProjectName', 'TopK', 'Precision', 'Recall', 'F1', 'F2']].sort_values(by=['Approach', 'ProjectName']).to_string(index=False))

# (5) Extract all rows from original df that use the best topK per approach
df_with_best = pd.merge(df, best_avg_topK[['Approach', 'Best_TopK']], on='Approach')
selected_rows = df_with_best[df_with_best['TopK'] == df_with_best['Best_TopK']]
selected_rows = selected_rows.sort_values(by=['Approach', 'ProjectName'])

# Output selected rows
print("\n=== All Rows Using Best TopK per Approach (Across All Projects) ===")
print(selected_rows[['Approach', 'ProjectName', 'TopK', 'Precision', 'Recall', 'F1', 'F2']].to_string(index=False))


from collections import defaultdict
import numpy as np

# Define project order
project_order = ['CM1-NASA', 'Dronology', 'GANNT', 'MODIS', 'WARC']
project_display = ['CM1', 'Dronology', 'GANNT', 'MODIS', 'WARC']

# Helper: format float
from decimal import Decimal, ROUND_HALF_UP
def fmt(x):
    if x is None or pd.isna(x):
        return "-"
    try:
        return f"{Decimal(str(x)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP):.2f}"
    except:
        return "-"

def make_latex_row(label, df_subset):
    by_project = defaultdict(lambda: {'P': None, 'R': None})
    avg_prec, avg_rec, avg_f1, avg_f2 = [], [], [], []

    for _, row in df_subset.iterrows():
        proj = row['ProjectName']
        by_project[proj]['P'] = row['Precision']
        by_project[proj]['R'] = row['Recall']
        by_project[proj]['F1'] = row['F1']
        by_project[proj]['F2'] = row['F2']
        avg_prec.append(row['Precision'])
        avg_rec.append(row['Recall'])
        avg_f1.append(row['F1'])
        avg_f2.append(row['F2'])

    line = f"{label}"
    for proj_key in project_order:
        p = fmt(by_project[proj_key]['P'])
        r = fmt(by_project[proj_key]['R'])
        f1 = fmt(by_project[proj_key]['F1'])
        f2 = fmt(by_project[proj_key]['F2'])
        line += f" & {p} & {r} & {f2}"
    line += f" & {fmt(np.mean(avg_prec))} & {fmt(np.mean(avg_rec))} & {fmt(np.mean(avg_f1))}  & {fmt(np.mean(avg_f2))} \\\\"
    return line

print()
print("For Latex Table:")
print()

# Filter for LSI and VSM separately
for approach in ['Embeddings']:
    # Best topK per approach
    df_fixed = selected_rows[selected_rows['Approach'] == approach]
    print(make_latex_row(f"{approach}\\textsubscript{{GO}}", df_fixed))

    # Best topK per project
    df_best = best_per_project[best_per_project['Approach'] == approach]
    print(make_latex_row(f"{approach}\\textsubscript{{PO}}", df_best))
