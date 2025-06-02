import pandas as pd
import numpy as np
import re
from collections import defaultdict

# --- Config ---
display_names = {
    "modisdataset": "MODIS",
    "dronology": "Dronology",
    "cm1-nasa": "CM1",
    "gannt": "GANNT",
    "warc": "WARC"
}

approach_renames = {
    "mv": "Majority Voting",
    "mv-gpt4o-mini": "Majority Voting + GPT-4o mini",
    "and": "Chaining",
    "and-gpt4o-mini": "Chaining + GPT-4o mini",
    "and-gpt4o": "Chaining + GPT-4o"
}

ordered_approaches = [
    "gemma2-2b", "gemma2-9b", "mistral-nemo", "phi4",
    "Majority Voting", "Chaining",
    "Majority Voting + GPT-4o mini",
    "Chaining + GPT-4o mini", "Chaining + GPT-4o"
]

project_order = ["CM1", "Dronology", "GANNT", "MODIS", "WARC", "Average"]

# --- Helper Functions ---
def extract_metadata(filename):
    filename_lower = filename.lower()
    dataset_match = None

    for key in display_names.keys():
        if key in filename_lower:
            dataset_match = key
            break

    if not dataset_match:
        raise ValueError(f"Could not determine dataset from filename: {filename}")

    # Remove everything up to and including the dataset match
    after_dataset = filename_lower.split(dataset_match, 1)[-1]
    after_dataset = re.sub(r'^[-_.]+', '', after_dataset)  # Trim leading separators
    approach = after_dataset.split(".json")[0]

    return dataset_match, approach


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
    for proj_key in project_order[:-1]:  # Skip "Average" in per-project loop
        p = fmt(by_project[proj_key]['P'])
        r = fmt(by_project[proj_key]['R'])
        f1 = fmt(by_project[proj_key]['F1'])
        f2 = fmt(by_project[proj_key]['F2'])
        line += f" & {p} & {r} & {f2}"
    line += f" & {fmt(np.mean(avg_prec))} & {fmt(np.mean(avg_rec))} & {fmt(np.mean(avg_f1))} & {fmt(np.mean(avg_f2))} \\\\"
    return line

# --- Main Processing ---
df = pd.read_csv("results.csv")

# Add F2 score
df["F2"] = (5 * df["Precision"] * df["Recall"]) / (4 * df["Precision"] + df["Recall"])

# Extract dataset and approach
df[["Dataset", "ApproachRaw"]] = df["File"].apply(lambda x: pd.Series(extract_metadata(x)))

# Map to project and approach names
df["ProjectName"] = df["Dataset"].map(display_names).fillna(df["Dataset"].str.upper())
df["Approach"] = df["ApproachRaw"].map(approach_renames).fillna(df["ApproachRaw"])

# Sort by custom approach order
df["Approach"] = pd.Categorical(df["Approach"], categories=ordered_approaches, ordered=True)
df.sort_values(by="Approach", inplace=True)

# Generate and print LaTeX rows
for approach in df["Approach"].cat.categories:
    subset = df[df["Approach"] == approach]
    if not subset.empty:
        print(make_latex_row(approach, subset))
