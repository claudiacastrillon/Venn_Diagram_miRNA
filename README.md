# 🧬 Venn Diagram Analysis for miRNA Expression
📌 Overview

This repository contains a Python script for filtering and visualizing miRNA expression overlaps using a Venn diagram. The goal is to identify miRNAs that are common across three pairwise comparisons and highlight key miRNAs for further analysis.

🔬 Methodology

Filtering Criteria:

Base mean expression > 450.

Fold change ≥ 2 for upregulated genes.

Fold change ≤ -2 for downregulated genes.

Adjusted P-value (FDR < 0.05) across all three comparisons.

Venn Diagram Generation:

Uses matplotlib and venn3 from matplotlib_venn.

Visualizes overlapping miRNAs among the three comparisons.

Adds a table listing common miRNAs to the right of the diagram.

📦 Dependencies

Ensure you have the following Python libraries installed:

pip install matplotlib matplotlib-venn pandas

🛠️ Usage

1️⃣ Clone this repository:

git clone https://github.com/claudiacastrillon/Venn_Diagram_miRNA.git

2️⃣ Navigate to the project folder:

cd Venn_Diagram_miRNA

3️⃣ Run the Python script:

python diagramavennpython.py

📊 Output

Venn Diagram illustrating overlapping miRNAs.

List of miRNAs in common and unique to each group.

Table with detailed miRNA information.

🤝 Contributions

Feel free to contribute by submitting pull requests or reporting issues!

📜 License

This project is open-source. See LICENSE for details.

📩 Contact

For inquiries, contact claudiacastrillon via GitHub. 💡
