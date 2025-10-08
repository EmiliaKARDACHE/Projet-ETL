import pandas as pd

# Chemin du fichier
csv_path = r"C:\Users\emili\OneDrive\Bureau\Projet-ETL\data\raw\AGRIBALYSE\extract_AGB32_agricole_conv.csv"
df = pd.read_csv(csv_path, sep=None, engine="python", encoding="utf-8")

# Statistiques descriptives
print("Statistiques descriptives :")
print(df.describe(include='all'))  # Remplace 'display' par 'print'

df = df.drop(columns=['LCI Name'])

# Colonnes entièrement vides
colonnes_vides = df.columns[df.isnull().all()]
if len(colonnes_vides) > 0:
    print("Colonnes entièrement vides :", list(colonnes_vides))
    df = df.drop(columns=colonnes_vides)

# Lignes entièrement vides
lignes_vides = df.index[df.isnull().all(axis=1)]
if len(lignes_vides) > 0:
    print("Numéros de lignes entièrement vides :", list(lignes_vides))
    df = df.drop(index=lignes_vides)

# Colonnes avec plus de 80% de NaN
seuil = 0.8
colonnes_nan80 = df.columns[df.isnull().mean() > seuil]
if len(colonnes_nan80) > 0:
    print("Colonnes avec plus de 80% de NaN :", list(colonnes_nan80))
    df = df.drop(columns=colonnes_nan80)

# Colonnes mal formatées (types mixtes)
colonnes_mal_formatees = [col for col in df.columns if df[col].apply(type).nunique() > 1]
if len(colonnes_mal_formatees) > 0:
    print("Colonnes mal formatées :", colonnes_mal_formatees)
    # On ne supprime pas ces colonnes

# Lignes mal formatées (longueur différente du nombre de colonnes)
lignes_mal_formatees = [i for i, row in df.iterrows() if len(row) != len(df.columns)]
if len(lignes_mal_formatees) > 0:
    print("Numéros de lignes mal formatées :", lignes_mal_formatees)
    # On ne supprime pas ces lignes

# Affiche le DataFrame nettoyé
print(df.head(10))

# Sauvegarde le DataFrame nettoyé dans un nouveau fichier
df.to_csv(r"C:\Users\emili\OneDrive\Bureau\Projet-ETL\data\raw\AGRIBALYSE\extract_AGB32_agricole_conv_clean.csv", index=False)
  