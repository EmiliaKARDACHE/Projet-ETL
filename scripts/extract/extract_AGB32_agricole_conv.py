import pandas as pd

excel_path = r"C:\Users\emili\OneDrive\Bureau\Projet-ETL\data\raw\AGRIBALYSE\AGB32_agriculture_conv.xlsx"
sheet_name = "AGB 3.2 agricole conventionnel"

# Ignore les deux premières lignes du fichier Excel
df = pd.read_excel(excel_path, sheet_name=sheet_name, skiprows=2)

# Nettoyage : supprime les colonnes et lignes entièrement vides
df = df.dropna(axis=1, how='all')
df = df.dropna(axis=0, how='all')
df = df.reset_index(drop=True)

# Renomme les colonnes : garde les 4 premières, puis applique les nouveaux noms + unités
nouveaux_noms = [
    "Score unique EF3.1 (mPt/kg)",
    "Changement climatique (kg CO2 eq/kg)",
    "Appauvrissement de la couche d'ozone (kg CFC11 eq/kg)",
    "Rayonnements ionisants (kBq U-235 eq/kg)",
    "Formation photochimique d'ozone (kg NMVOC eq/kg)",
    "Particules (disease inc./kg)",
    "Effets toxicologiques sur la santé humaine : substances non-cancérogènes* (CTUh/kg)",
    "Effets toxicologiques sur la santé humaine : substances cancérogènes* (CTUh/kg)",
    "Acidification terrestre et eaux douces (mol H+ eq/kg)",
    "Eutrophisation eaux douces (kg P eq/kg)",
    "Eutrophisation marine (kg N eq/kg)",
    "Eutrophisation terreste (mol N eq/kg)",
    "Écotoxicité pour écosystèmes aquatiques d'eau douce (CTUe/kg)",
    "Utilisation du sol (Pt/kg)",
    "Épuisement des ressources eau (m3 depriv./kg)",
    "Épuisement des ressources énergétiques (MJ/kg)",
    "Épuisement des ressources minéraux (kg Sb eq/kg)",
    "Changement climatique - émissions biogéniques (kg CO2 eq/kg)",
    "Changement climatique - émissions fossiles (kg CO2 eq/kg)",
    "Changement climatique - émissions liées au changement d'affectation des sols (kg CO2 eq/kg)"
]

colonnes = list(df.columns)
colonnes[:4] = colonnes[:4]  # garde les 4 premiers noms
colonnes[4:4+len(nouveaux_noms)] = nouveaux_noms
df.columns = colonnes

# Sauvegarde propre
df.to_csv(r"C:\Users\emili\OneDrive\Bureau\Projet-ETL\data\raw\AGRIBALYSE\extract_AGB32_agricole_conv.csv", index=False) 