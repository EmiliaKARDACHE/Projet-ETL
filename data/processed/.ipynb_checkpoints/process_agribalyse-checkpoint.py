
import pandas as pd
import matplotlib.pyplot as plt

# Chemin du fichier : Agribalyse_detail_par_ingredient
#csv_path = r"C:\Users\emili\OneDrive\Bureau\Projet-ETL\data\raw\AGRIBALYSE\Agribalyse_detail_par_ingredient.csv"
#Lecture (auto-détection du séparateur)
#df = pd.read_csv(csv_path, sep=None, engine="python", encoding="utf-8") 
#print (df.head(10))

# Chemin du fichier : AGB32_agricole_conventionnel
csv_path1 = r"C:\Users\emili\OneDrive\Bureau\Projet-ETL\data\raw\AGRIBALYSE\AGB32_agricole_conventionnel.csv"
# Lecture (auto-détection du séparateur)
df = pd.read_csv(csv_path1, sep=None, engine="python", encoding="utf-8") 
print (df.head(10))   


