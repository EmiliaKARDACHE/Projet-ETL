import pandas as pd
import matplotlib.pyplot as plt

# 👉 Chemin de ton fichier
xls_path = r"C:\Users\emili\OneDrive\Bureau\Projet-ETL\data\raw\AGRIBALYSE\Méthodologie Alimentation Annexes_AGB 3.2.xlsx"

# 1) Lire la première feuille (par défaut)
df = pd.read_excel(xls_path)
print(df.head())

