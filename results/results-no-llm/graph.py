import pandas as pd
import matplotlib.pyplot as plt
import re
from matplotlib import rcParams

# Load no-LLM results
df_no_llm = pd.read_csv("results-no-llm.csv")

def extract_project(filename):
    match = re.search(r"results-(.*?)(_no_llm|-no_llm)", filename)
    name = match.group(1) if match else "Unknown"
    return "MODIS" if name == "ModisDataset" else name[0].upper() + name[1:]

df_no_llm['Project'] = df_no_llm['File'].apply(extract_project)

# Load LLM-Ensembled results
df_llm = pd.read_csv("../results/results.csv")

max_combinations = {
    "CM1-NASA": 1166,
    "dronology": 20889,
    "GANNT": 1173,
    "ModisDataset": 931,
    "WARC": 5607
}
display_names = {
    "ModisDataset": "MODIS"
}

def extract_llm_project(filename):
    for key in max_combinations:
        pattern = f"results-{key}-"
        if pattern in filename:
            name = display_names.get(key, key)
            return "Dronology" if name == "dronology" else name
    return "Unknown"

df_llm['Project'] = df_llm['File'].apply(extract_llm_project)

# Define consistent color map for the 5 projects using default Matplotlib colors
default_colors = rcParams['axes.prop_cycle'].by_key()['color']
project_order = ['CM1-NASA', 'Dronology', 'GANNT', 'MODIS', 'WARC']
color_map = {proj: default_colors[i] for i, proj in enumerate(project_order)}

# -------- Plot 1: No-LLM only --------
plt.figure(figsize=(10, 6))
for project, group in df_no_llm.groupby('Project'):
    color = color_map.get(project, 'gray')
    plt.scatter(group['Recall'], group['Precision'], label=project, marker='o', color=color, zorder=3)

plt.title('Retrieval using Text Embeddings')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.xlim(-0.1, 1.1)
plt.ylim(-0.1, 1.1)
plt.grid(True)
plt.legend(title="Project", loc='upper right', frameon=True)
plt.tight_layout()
plt.savefig("precision_recall_by_project.pdf")
print("[INFO] Plot saved as precision_recall_by_project.pdf")

# -------- Plot 2: Combined with LLM-Ensembled --------
plt.figure(figsize=(10, 6))

# No-LLM results
for project, group in df_no_llm.groupby('Project'):
    color = color_map.get(project, 'gray')
    plt.scatter(group['Recall'], group['Precision'], label=project, marker='o', color=color, zorder=3)

# LLM-Ensembled results
for project, group in df_llm.groupby('Project'):
    color = color_map.get(project, 'gray')
    plt.scatter(group['Recall'], group['Precision'], label=f"{project} (LLM)", marker='x',
                s=60, linewidths=1.5, color=color, zorder=4)

plt.title('Precision–Recall Plot: Text Embeddings vs LLM-Ensembled')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.xlim(-0.1, 1.1)
plt.ylim(-0.1, 1.1)
plt.grid(True)
plt.legend(title="Project", loc='upper right', frameon=True)
plt.tight_layout()
plt.savefig("precision_recall_with_llm.pdf")
print("[INFO] Plot saved as precision_recall_with_llm.pdf")
