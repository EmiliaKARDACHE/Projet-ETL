import pandas as pd

excel_path = r"C:\Users\emili\OneDrive\Bureau\Projet-ETL\data\raw\AGRIBALYSE\AGRIBALYSE3.2_partie agriculture_conv_PublieAOUT25.xlsx"
sheet_name = "AGB 3.2 agricole conventionnel"

# Ignore les deux premières lignes du fichier Excel
df = pd.read_excel(excel_path, sheet_name=sheet_name, skiprows=2)

# Nettoyage : supprime les colonnes et lignes entièrement vides
df = df.dropna(axis=1, how='all')
df = df.dropna(axis=0, how='all')
df = df.reset_index(drop=True)

# Noms des colonnes à partir de la 5e colonne (index 4)
nouveaux_noms = [
    "Score unique EF3.1",
    "Changement climatique",
    "Appauvrissement de la couche d'ozone",
    "Rayonnements ionisants",
    "Formation photochimique d'ozone",
    "Particules",
    "Effets toxicologiques sur la santé humaine : substances non-cancérogènes*",
    "Effets toxicologiques sur la santé humaine : substances cancérogènes*",
    "Acidification terrestre et eaux douces",
    "Eutrophisation eaux douces",
    "Eutrophisation marine",
    "Eutrophisation terreste",
    "Écotoxicité pour écosystèmes aquatiques d'eau douce",
    "Utilisation du sol",
    "Épuisement des ressources eau",
    "Épuisement des ressources énergétiques",
    "Épuisement des ressources minéraux",
    "Changement climatique - émissions biogéniques",
    "Changement climatique - émissions fossiles",
    "Changement climatique - émissions liées au changement d'affectation des sols"
]

# Unités à ajouter en sous-noms (pour info, pas obligatoire dans le header)
unites = [
    "mPt/kg", "kg CO2 eq/kg", "kg CFC11 eq/kg", "kBq U-235 eq/kg", "kg NMVOC eq/kg",
    "disease inc./kg", "CTUh/kg", "CTUh/kg", "mol H+ eq/kg", "kg P eq/kg",
    "kg N eq/kg", "mol N eq/kg", "CTUe/kg", "Pt/kg", "m3 depriv./kg", "MJ/kg",
    "kg Sb eq/kg", "kg CO2 eq/kg", "kg CO2 eq/kg", "kg CO2 eq/kg"
]

# Renomme les colonnes : garde les 4 premières, puis applique les nouveaux noms
colonnes = list(df.columns)
colonnes[:4] = colonnes[:4]  # garde les 4 premiers noms
colonnes[4:4+len(nouveaux_noms)] = nouveaux_noms
df.columns = colonnes

# Sauvegarde propre
df.to_csv(r"C:\Users\emili\OneDrive\Bureau\Projet-ETL\data\raw\AGRIBALYSE\AGB32_agricole_conventionnel.csv", index=False)