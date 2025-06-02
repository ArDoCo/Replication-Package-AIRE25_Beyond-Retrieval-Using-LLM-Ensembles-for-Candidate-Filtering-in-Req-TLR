import pandas as pd

# Load the CSV file
df = pd.read_csv('Baselines_R2R-evaluation.csv')

# Ensure correct data types
df['Threshold'] = pd.to_numeric(df['Threshold'], errors='coerce')
df['F2'] = pd.to_numeric(df['F2'], errors='coerce')

# Sort for consistency
df = df.sort_values(by='Threshold')

# (1) Best threshold per project (max F2 per project-approach)
best_per_project = df.loc[df.groupby(['ProjectName', 'Approach'])['F2'].idxmax()]

# (2) Compute average F2 per approach-threshold pair
avg_f2_per_threshold = df.groupby(['Approach', 'Threshold'])['F2'].mean().reset_index()

# (3) For each approach, find the threshold with the highest average F2
best_avg_threshold = avg_f2_per_threshold.loc[avg_f2_per_threshold.groupby('Approach')['F2'].idxmax()]
best_avg_threshold.columns = ['Approach', 'Best_Threshold', 'Average_Best_F2']

# Output summary
print("\n=== Best Threshold per Approach Based on Highest Average F2 Across Projects ===")
print(best_avg_threshold)

# (4) Output best thresholds per project (as originally computed)
print("\n=== Best Threshold per Project and Approach (Based on Max F2) ===")
print(best_per_project[['Approach', 'ProjectName', 'Threshold', 'Precision', 'Recall', 'F1', 'F2']].sort_values(by=['Approach', 'ProjectName']).to_string(index=False))

# (5) Extract all rows from original df that use the best threshold per approach
df_with_best = pd.merge(df, best_avg_threshold[['Approach', 'Best_Threshold']], on='Approach')
selected_rows = df_with_best[df_with_best['Threshold'] == df_with_best['Best_Threshold']]
selected_rows = selected_rows.sort_values(by=['Approach', 'ProjectName'])

# Output selected rows
print("\n=== All Rows Using Best Threshold per Approach (Across All Projects) ===")
print(selected_rows[['Approach', 'ProjectName', 'Threshold', 'Precision', 'Recall', 'F1', 'F2']].to_string(index=False))


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
for approach in ['VSM', 'LSI']:
    # Best threshold per approach
    df_fixed = selected_rows[selected_rows['Approach'] == approach]
    print(make_latex_row(f"{approach}\\textsubscript{{GO}}", df_fixed))

    # Best threshold per project
    df_best = best_per_project[best_per_project['Approach'] == approach]
    print(make_latex_row(f"{approach}\\textsubscript{{PO}}", df_best))
