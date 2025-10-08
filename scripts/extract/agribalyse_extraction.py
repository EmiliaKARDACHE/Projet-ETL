# scripts/extract/agribalyse_extraction.py

import os
import pandas as pd

def extract_agribalyse_excel_to_csv():
    # --- Chemins ---
    excel_path = "../../data/raw/AgriBalyse/AGRIBALYSE3.2_Tableur agriculture_bio_PublieNov24.xlsx"
    sheet_name = "AGB 3.2 agricole biologique"
    output_dir = "../../data/raw/AgriBalyse"
    output_file = os.path.join(output_dir, "agribalyse_agriculture_biologique_extraction.csv")

    # Création du répertoire de sortie s'il n'existe pas
    os.makedirs(output_dir, exist_ok=True)

    print(f"Lecture du fichier Excel : {excel_path}")
    print(f"Feuille ciblée : {sheet_name}")

    # Lecture du tableau avec en-tête sur deux lignes (ligne 2 et 3 du fichier Excel)
    # skiprows=1 => on ignore la première ligne (index Excel = 1, car pandas commence à 0)
    df = pd.read_excel(
        excel_path,
        sheet_name=sheet_name,
        header=1,   # ligne 2 et 3 (Excel) → fusion de headers
        usecols="A:X",   # colonnes A à X
        skiprows=1,      # pour que la ligne 2 soit bien la première du header
        nrows=226        # 229 - 3 = 226 lignes de données
    )

    print("Aperçu des en-têtes détectés :")
    print(df.columns.tolist())

    print(f"Export du tableau ({df.shape[0]} lignes, {df.shape[1]} colonnes)")
    df.to_csv(output_file, index=False, sep=";", encoding="utf-8-sig")

    print(f"✅ Extraction terminée ! Fichier CSV créé : {output_file}")


if __name__ == "__main__":
    extract_agribalyse_excel_to_csv()
