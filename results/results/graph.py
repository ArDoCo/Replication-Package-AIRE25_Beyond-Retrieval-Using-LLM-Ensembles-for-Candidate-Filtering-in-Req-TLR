import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams.update({
    'font.size': 14,
    'font.family': 'serif',
    'font.serif': ['Times']
})

# Load CSV
df = pd.read_csv("results.csv")
print(f"[INFO] Loaded {len(df)} rows from results.csv")

# Known maximum number of combinations per project
max_combinations = {
    "CM1-NASA": 1166,
    "dronology": 20889,
    "GANNT": 1173,
    "ModisDataset": 931,
    "WARC": 5607
}

# Display name mapping
display_names = {
    "ModisDataset": "MODIS",
    "dronology": "Dronology"
}

# Approach renaming
approach_renames = {
    "gemma2-2b": "Gemma-2:2b",
    "gemma2-9b": "Gemma-2:9b",
    "mistral-nemo": "Mistral-Nemo:12b",
    "phi4": "Phi-4:14b",
    "mv": "Majority Voting",
    "mv-gpt4o-mini": "MV + GPT-4o mini",
    "and": "Chaining",
    "and-gpt4o-mini": "Chaining + GPT-4o mini",
    "and-gpt4o": "Chaining + GPT-4o"
}

# Approach display order
ordered_approaches = [
    "Gemma-2:2b", "Gemma-2:9b", "Mistral-Nemo:12b", "Phi-4:14b",  # Group A
    "Chaining", "Majority Voting",                      # Group B (simple)
    #"MV + GPT-4o mini",
    #"Chaining + GPT-4o mini", "Chaining + GPT-4o"  # Group B (w/ GPT-4o)
]

# Extract Project and Approach
def extract_project_and_approach(filename):
    for project_key in max_combinations:
        pattern = f"results-{project_key}-"
        if pattern in filename:
            approach = filename.split(pattern)[1].split(".json")[0]
            display_project = display_names.get(project_key, project_key)
            renamed = approach_renames.get(approach, approach)
            return display_project, renamed
    print(f"[WARN] Project not recognized in: {filename}")
    return "Unknown", "Unknown"

# Apply extraction
df[['Project', 'Approach']] = df['File'].apply(lambda x: pd.Series(extract_project_and_approach(x)))

# Compute retrieved combinations
df['Retrieved'] = df['True Positives'] + df['False Positives']

# Map max combinations
def map_max(project_display_name):
    reverse_map = {v: k for k, v in display_names.items()}
    original_key = reverse_map.get(project_display_name, project_display_name)
    return max_combinations.get(original_key, None)

df['Max'] = df['Project'].apply(map_max)
df['Fraction'] = df['Retrieved'] / df['Max']

# Debug: list approaches
print("[INFO] Unique Project–Approach pairs:")
print(df[['Project', 'Approach']].drop_duplicates().to_string(index=False))

# Pivot and reorder
pivot = df.groupby(['Project', 'Approach'])['Fraction'].mean().unstack().fillna(0)

# Keep only approaches in the defined order
pivot = pivot[[a for a in ordered_approaches if a in pivot.columns]]

# Compute mean recall and retrieved values per (Project, Approach)
recall_pivot = df.groupby(['Project', 'Approach'])['Recall'].mean().unstack().fillna(0)
retrieved_pivot = df.groupby(['Project', 'Approach'])['Retrieved'].mean().unstack().fillna(0)
recall_pivot = recall_pivot[[a for a in ordered_approaches if a in recall_pivot.columns]]
retrieved_pivot = retrieved_pivot[[a for a in ordered_approaches if a in retrieved_pivot.columns]]

# Plot
fig, ax = plt.subplots(figsize=(12, 4.7))
bars = pivot.plot(kind='bar', ax=ax, width=0.8, zorder=3)

# Right y-axis for recall
ax_recall = ax.twinx()
ax.set_ylim(0, 1.199)
ax_recall.set_ylim(0, 1.199)
ax.set_ylabel('Fraction of Retrieved Pairs (TP + FP) / Total')
ax_recall.set_ylabel('Recall')
ax_recall.tick_params(axis='y')

# Annotate with recall diamonds and labels
for idx, project in enumerate(pivot.index):
    for j, approach in enumerate(pivot.columns):
        height = pivot.loc[project, approach]
        recall_val = recall_pivot.loc[project, approach]
        retrieved_val = int(retrieved_pivot.loc[project, approach])

        if height > 0 and recall_val <= 1.0:
            bar_offset = (j - len(pivot.columns) / 2 + 0.5) * (0.8 / len(pivot.columns))
            x_pos = idx + bar_offset
            bar = bars.containers[j][idx]
            color = bar.get_facecolor()

            ax_recall.scatter(
                x_pos, recall_val,
                marker='D',
                s=50,
                facecolors='none',
                edgecolors=color,
                linewidths=1.2,
                zorder=5
            )

            ax_recall.text(
                x_pos,
                recall_val + 0.025,
                f"R={recall_val:.2f}",
                ha='center',
                va='bottom',
                rotation=90,
                fontsize=12,
                zorder=6
            )

# Project labels
project_labels = [
    f"{proj}\n(Total={int(df[df['Project'] == proj]['Max'].iloc[0])})"
    for proj in pivot.index
]
ax.set_xticks(range(len(project_labels)))
ax.set_xticklabels(project_labels, rotation=0)

# Final styling
ax.grid(True, axis='y', linestyle='--', alpha=0.7)
ax.legend(title='Mode', bbox_to_anchor=(1.075, 1), loc='upper left')
ax.set_xlabel(None)
plt.tight_layout()


# Save figure
plt.savefig("filtering_capability_by_approach.pdf")
print("[INFO] Plot saved as filtering_capability_by_approach.pdf")
