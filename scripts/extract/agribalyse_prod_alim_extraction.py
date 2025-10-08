# scripts/extract/agribalyse_extraction.py

import os
import pandas as pd

def extract_agribalyse_excel_to_csv():
    # --- Chemins ---
    excel_path = "../../data/raw/AgriBalyse/AGRIBALYSE3.2_Tableur produits alimentaires_PublieAOUT25.xlsx"
    sheet_name = "Detail ingredient"
    output_dir = "../../data/raw/AgriBalyse"
    output_file = os.path.join(output_dir, "agribalyse_detail_ingredient_extraction.csv")

    print(f"Lecture du fichier Excel : {excel_path}")
    print(f"Feuille ciblée : {sheet_name}")

    # Lecture du tableau en prenant uniquement la ligne 3 d’Excel comme header
    df = pd.read_excel(
        excel_path,
        sheet_name=sheet_name,
        header=2,       # ligne 3 d’Excel
        usecols="A:AD",  # colonnes A à 1D
        nrows=7269       # lignes 4 à 7272
    )

    print("Aperçu des en-têtes détectés :")
    print(df.columns.tolist())

    # --- Liste des nouveaux noms de colonnes à partir de la 5e ---
    new_names_from_10 = [
        "Score unique EF3.1 (mPt/kg)",
        "Changement climatique (kg CO2 eq/kg)",
        "Appauvrissement de la couche d'ozone (kg CFC11 eq/kg)",
        "Rayonnements ionisants (kBq U-235 eq/kg)",
        "Formation photochimique d’ozone (kg NMVOC eq/kg)",
        "Particules (disease inc./kg)",
        "Effets toxicologiques sur la santé humaine : substances non-cancérogènes* (CTUh/kg)",
        "Effets toxicologiques sur la santé humaine : substances cancérogènes* (CTUh/kg)",
        "Acidification terrestre et eaux douces (mol H+ eq/kg)",
        "Eutrophisation eaux douces (kg P eq/kg)",
        "Eutrophisation marine (kg N eq/kg)",
        "Eutrophisation terrestre (mol N eq/kg)",
        "Écotoxicité pour écosystèmes aquatiques d’eau douce (CTUe/kg)",
        "Utilisation du sol (Pt/kg)",
        "Épuisement des ressources en eau (m³ depriv./kg)",
        "Épuisement des ressources énergétiques (MJ/kg)",
        "Épuisement des ressources en minéraux (kg Sb eq/kg)",
        "Changement climatique - émissions biogéniques (kg CO2 eq/kg)",
        "Changement climatique - émissions fossiles (kg CO2 eq/kg)",
        "Changement climatique - émissions liées au changement d’affectation des sols (kg CO2 eq/kg)"
    ]

    # --- Vérification du nombre de colonnes ---
    if len(df.columns) < 10 + len(new_names_from_10):
        raise ValueError(
            f"Le DataFrame contient {len(df.columns)} colonnes, "
            f"mais {10 + len(new_names_from_10)} sont nécessaires pour appliquer le renommage."
        )

    # --- Renommage des colonnes ---
    df.columns = list(df.columns[:10]) + new_names_from_10

    # --- Aperçu du DataFrame après renommage ---
    print("Aperçu des colonnes après renommage :")
    print(df.columns.tolist())

    # --- Export en CSV ---
    df.to_csv(output_file, index=False, sep=";", encoding="utf-8-sig")
    print(f"✅ Extraction et renommage terminés ! Fichier CSV créé : {output_file}")


if __name__ == "__main__":
    extract_agribalyse_excel_to_csv()
