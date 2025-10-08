import os
import pandas as pd

# Détermination des chemins relatifs depuis le script
base_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.join(base_dir, "..", "..")

# Chemins d’entrée et de sortie
csv_path = os.path.join(root_dir, "data", "raw", "AgriBalyse", "Agribalyse_detail_ingredient_extraction.csv")
output_path = os.path.join(root_dir, "data", "processed", "agribalyse_detail_par_ingredient.csv")

# Lecture du fichier CSV
df = pd.read_csv(csv_path, sep=';', encoding="utf-8-sig")

# Colonnes à supprimer
colonnes_a_supprimer = [
    "Ciqual code",
    "LCI Name",
]

df.drop(columns=colonnes_a_supprimer, inplace=True, errors="ignore")

# Nettoyage : suppression des lignes vides et doublons
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# Nettoyage des espaces inutiles dans les colonnes texte
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip()

# Sauvegarde du fichier nettoyé
os.makedirs(os.path.dirname(output_path), exist_ok=True)
df.to_csv(output_path, index=False, encoding="utf-8-sig")

print(f"✅ Fichier nettoyé enregistré dans : {output_path}")
