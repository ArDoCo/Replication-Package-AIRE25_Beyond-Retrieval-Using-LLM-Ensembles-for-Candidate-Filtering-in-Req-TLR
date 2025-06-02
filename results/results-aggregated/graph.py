import pandas as pd
import matplotlib.pyplot as plt
import re
import matplotlib

matplotlib.rcParams.update({
    'font.size': 22,
    'font.family': 'serif',
    'font.serif': ['Times']
})

# Load both CSV files
llm_df = pd.read_csv("../results-no-llm/results-no-llm.csv")
baseline_df = pd.read_csv("../results-vsm-lsi/Baselines_R2R-evaluation.csv")

# Extract project names from filenames in LLM results
def extract_project(filename):
    match = re.search(r"results-(.*?)(_no_llm|-no_llm)", filename)
    name = match.group(1) if match else "Unknown"
    if name == "ModisDataset":
        name = "MODIS"
    return name[0].upper() + name[1:]

llm_df['ProjectName'] = llm_df['File'].apply(extract_project)
llm_df['Approach'] = 'Embeddings'

# Keep columns consistent across both datasets
llm_df = llm_df[['ProjectName', 'Approach', 'Precision', 'Recall']]
baseline_df = baseline_df[['ProjectName', 'Approach', 'Precision', 'Recall', 'Threshold']]

# Combine the two datasets
combined_df = pd.concat([llm_df, baseline_df], ignore_index=True)

# Get unique projects
projects = combined_df['ProjectName'].unique()

# Define markers and z-order for each approach
marker_map = {'Embeddings': 'o', 'VSM': 's', 'LSI': '^'}
zorder_map = {'Embeddings': 4, 'VSM': 3, 'LSI': 2}

# Plot each project without the legend
for project in projects:
    plt.figure(figsize=(6, 4))
    project_df = combined_df[combined_df['ProjectName'] == project]

    for approach, group in project_df.groupby('Approach'):
        marker = marker_map.get(approach, 'x')
        zorder = zorder_map.get(approach, 0)
        plt.scatter(group['Recall'], group['Precision'], marker=marker, label=approach, zorder=zorder)

    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.xlim(-0.1, 1.1)
    plt.ylim(-0.1, 1.1)
    plt.grid(True)
    plt.tight_layout()

    # Save without legend
    filename = f"precision_recall_{project.replace(' ', '_')}.pdf"
    plt.savefig(filename)
    plt.close()

# Create and save a separate legend figure
fig, ax = plt.subplots(figsize=(3, 2))  # Adjust size as needed
handles = []
labels = []

for approach in marker_map:
    handle = ax.scatter([], [], marker=marker_map[approach], label=approach, s=100)
    handles.append(handle)
    labels.append(approach)

legend = ax.legend(handles=handles, labels=labels, title="Approach", loc='center', frameon=True)
ax.axis('off')

plt.tight_layout()
plt.savefig("legend_only.pdf")
plt.close()
