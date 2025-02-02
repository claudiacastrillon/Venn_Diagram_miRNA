import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pandas as pd

# Define sets for each comparison
mild_vs_severe = {
    "hsa-miR-223-3p", "hsa-miR-223-5p", "hsa-miR-1307-3p", "hsa-miR-1246",
    "hsa-miR-142-5p", "hsa-miR-143-3p", "hsa-miR-151a-3p", "hsa-miR-221-3p",
    "hsa-miR-199a-3p", "hsa-miR-197-3p", "hsa-miR-193a-5p", "hsa-miR-4508",
    "hsa-miR-191-5p", "hsa-miR-148a-3p", "hsa-miR-24-3p", "hsa-miR-26b-5p",
    "hsa-miR-23a-3p", "hsa-miR-484", "hsa-miR-150-5p", "hsa-miR-126-3p",
    "hsa-let-7f-5p"
}

moderate_vs_severe = {
    "hsa-miR-223-3p", "hsa-miR-143-3p", "hsa-miR-182-5p", "hsa-miR-142-5p",
    "hsa-miR-223-5p", "hsa-miR-24-3p", "hsa-miR-199a-3p", "hsa-miR-197-3p",
    "hsa-let-7f-5p", "hsa-miR-221-3p", "hsa-miR-29a-3p", "hsa-miR-122-5p",
    "hsa-miR-484", "hsa-miR-320d", "hsa-miR-1307-3p", "hsa-miR-30a-5p",
    "hsa-miR-4508", "hsa-miR-148a-3p", "hsa-miR-148b-3p", "hsa-miR-146a-5p",
    "hsa-miR-23a-3p", "hsa-miR-103a-3p", "hsa-miR-1246", "hsa-miR-151a-3p",
    "hsa-miR-193a-5p", "hsa-miR-25-3p"
}

mild_moderate_vs_severe = {
    "hsa-miR-223-3p", "hsa-miR-223-5p", "hsa-miR-1307-3p", "hsa-miR-1246",
    "hsa-miR-142-5p", "hsa-miR-143-3p", "hsa-miR-151a-3p", "hsa-miR-221-3p",
    "hsa-miR-199a-3p", "hsa-miR-197-3p", "hsa-miR-193a-5p", "hsa-miR-182-5p",
    "hsa-miR-4508", "hsa-miR-191-5p", "hsa-miR-148a-3p", "hsa-miR-24-3p",
    "hsa-miR-23a-3p", "hsa-miR-484", "hsa-miR-30a-5p", "hsa-let-7f-5p",
    "hsa-miR-148b-3p", "hsa-miR-25-3p", "hsa-miR-29a-3p", "hsa-miR-122-5p",
    "hsa-miR-320d"
}

# Determine common and unique microRNAs
common_all = mild_vs_severe & moderate_vs_severe & mild_moderate_vs_severe
unique_mild_vs_severe = mild_vs_severe - (moderate_vs_severe | mild_moderate_vs_severe)
unique_moderate_vs_severe = moderate_vs_severe - (mild_vs_severe | mild_moderate_vs_severe)
unique_mild_moderate_vs_severe = mild_moderate_vs_severe - (mild_vs_severe | moderate_vs_severe)

# Create a DataFrame to display the results
max_len = max(len(common_all), len(unique_mild_vs_severe), len(unique_moderate_vs_severe), len(unique_mild_moderate_vs_severe))
df = pd.DataFrame({
    'Common to All': list(common_all) + [''] * (max_len - len(common_all)),
    'Unique to Mild vs Severe': list(unique_mild_vs_severe) + [''] * (max_len - len(unique_mild_vs_severe)),
    'Unique to Moderate vs Severe': list(unique_moderate_vs_severe) + [''] * (max_len - len(unique_moderate_vs_severe)),
    'Unique to Mild-Moderate vs Severe': list(unique_mild_moderate_vs_severe) + [''] * (max_len - len(unique_mild_moderate_vs_severe))
})


# Define colors for the circles
colors = ['red', 'green', 'blue']
alpha = 0.5

# Plot the custom Venn diagram and table
fig, ax = plt.subplots(1, 2, figsize=(18, 10))

# Create and position the circles manually
circle1 = patches.Circle((0.8, 0.8), 0.5, edgecolor=colors[0], facecolor=colors[0], alpha=alpha, linewidth=2)
circle2 = patches.Circle((1.2, 0.8), 0.5, edgecolor=colors[1], facecolor=colors[1], alpha=alpha, linewidth=2)
circle3 = patches.Circle((1, 1.2), 0.5, edgecolor=colors[2], facecolor=colors[2], alpha=alpha, linewidth=2)

ax[0].add_patch(circle1)
ax[0].add_patch(circle2)
ax[0].add_patch(circle3)

# Add labels manually
ax[0].text(0.6, 0.25, 'Mild vs Severe', horizontalalignment='center', verticalalignment='center', fontsize=12)
ax[0].text(1.3, 0.25, 'Moderate vs Severe', horizontalalignment='center', verticalalignment='center', fontsize=12)
ax[0].text(1.1, 1.8, 'Mild - Moderate vs Severe', horizontalalignment='center', verticalalignment='center', fontsize=12)

# Find the intersections and add counts manually
sets = [mild_vs_severe, moderate_vs_severe, mild_moderate_vs_severe]
counts = {
    '100': len(sets[0] - sets[1] - sets[2]), 
    '010': len(sets[1] - sets[0] - sets[2]), 
    '001': len(sets[2] - sets[0] - sets[1]), 
    '110': len(sets[0] & sets[1] - sets[2]), 
    '101': len(sets[0] & sets[2] - sets[1]), 
    '011': len(sets[1] & sets[2] - sets[0]), 
    '111': len(sets[0] & sets[1] & sets[2]), 
    '110': len(sets[0] & sets[1] - sets[2])
}

# Manually place counts
ax[0].text(0.6, 0.7, counts['100'], horizontalalignment='center', verticalalignment='center', fontsize=12)
ax[0].text(1.5, 0.7, counts['010'], horizontalalignment='center', verticalalignment='center', fontsize=12)
ax[0].text(1.0, 1.5, counts['001'], horizontalalignment='center', verticalalignment='center', fontsize=12)
ax[0].text(0.7, 1.2, counts['101'], horizontalalignment='center', verticalalignment='center', fontsize=12)
ax[0].text(1.3, 1.2, counts['011'], horizontalalignment='center', verticalalignment='center', fontsize=12)
ax[0].text(1.0, 1.0, counts['111'], horizontalalignment='center', verticalalignment='center', fontsize=12)
ax[0].text(1.0, 0.6, counts['110'], horizontalalignment='center', verticalalignment='center', fontsize=12)

ax[0].set_xlim(0, 2)
ax[0].set_ylim(0, 2)
ax[0].set_aspect('equal', 'box')
ax[0].axis('off')

# Set title
ax[0].set_title("Diagrama de Venn de microRNAs entre Grupos")

# Plot the table
ax[1].axis('off')
table = ax[1].table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.9, 1.5)

plt.tight_layout()
plt.show()
