import pandas as pd
csv_path = 'C:/user/grego/code/NotNemezis/Projet-ETL/data/raw/AGRIBALYSE/Agribalyse_detail_par_etape.csv'
df = pd.read_csv(csv_path)

colonnes_a_supprimer = [
    'Code CIQUAL',
    'LCI Name',
]

df.drop(columns=colonnes_a_supprimer, inplace=True)

df.dropna(inplace=True)

df.drop_duplicates(inplace=True)

for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].str.strip()

df.to_csv('C:/user/grego/code/NotNemezis/Projet-ETL/data/processed/agribalyse_detail_par_etape.csv', index=False)