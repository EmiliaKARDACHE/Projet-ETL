# scripts/extract/extract_all_sheets.py

import os
import pandas as pd

def extract_excel_sheets_to_csv():
    # --- Chemins ---
    excel_path = "../../data/raw/AgriBalyse/Méthodologie Alimentation Annexes_AGB 3.2.xlsx"
    output_dir = "../../data/processed/agb_methodology"
    os.makedirs(output_dir, exist_ok=True)

    # --- Configuration par feuille (pour les 11 feuillets à traiter, skip index 0) ---
    # clé = index du feuillet à traiter (1-based pour correspondre à sheet_names[1:])
    sheets_config = {
        1: {"header": 2, "usecols": "A:F", "nrows": 1532},
        2: {"header": 2, "usecols": "A:G", "nrows": 31},
        3: {"header": 3, "usecols": "A:D", "nrows": 73},
        4: {"header": 2, "usecols": "A:H", "nrows": 92},
        5: {"header": 3, "usecols": "A:C", "nrows": 17},
        6: {"header": 2, "usecols": "A:C", "nrows": 14},
        7: {"header": 2, "usecols": "A:G", "nrows": 28},
        8: {"header": 2, "usecols": "A:E", "nrows": 119},
        9: {"header": 3, "usecols": "A:J", "nrows": 1101},
        10: {"header": 2, "usecols": "A:E", "nrows": 410},
        11: {"header": 5, "usecols": "A:C", "nrows": 3181}
    }

    # --- Lire le fichier Excel pour obtenir la liste des feuilles ---
    xls = pd.ExcelFile(excel_path)
    sheet_names = xls.sheet_names

    # --- Boucle sur les 11 feuillets (index 1 à 11) ---
    for idx, config in sheets_config.items():
        sheet_name = sheet_names[idx]  # skip index 0, donc idx 1 → sheet_names[1]
        print(f"Extraction de la feuille {idx+1}: {sheet_name}")

        df = pd.read_excel(
            excel_path,
            sheet_name=sheet_name,
            header=config["header"],
            usecols=config["usecols"],
            nrows=config["nrows"]
        )

        # Nom du fichier CSV
        output_file = os.path.join(output_dir, f"{sheet_name}.csv")

        # Export CSV
        df.to_csv(output_file, index=False, sep=";", encoding="utf-8-sig")
        print(f"✅ Feuille '{sheet_name}' exportée vers {output_file}")

    print("✅ Toutes les feuilles sélectionnées ont été exportées !")

if __name__ == "__main__":
    extract_excel_sheets_to_csv()
