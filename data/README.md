# README Données — Traitement des données (brutes → traitées)

## 🎯 Objectif
Décrire comment les données brutes sont ingérées, nettoyées, transformées et stockées sous forme d’artéfacts prêts à être analysés ou consommés par des processus ETL.

## 📦 Conventions sur les données clean
- Formats de fichiers csv
- Convention de nommage : `<source>_<sujet>.csv`
- Les fichiers bruts sont immuables. Déplacez les nouveaux fichiers dans `data/raw/` pour qu’ils soient ingérés par le pipeline.

## 🔄 Étapes principales du pipeline

### 1. Parsing & normalisation
- Lecture du fichier CSV avec séparateur `;` depuis `data/raw/`.
- Normalisation des chaînes de caractères : suppression des espaces en début/fin de champ.
- Encodage supposé en UTF-8.
- Les formats de date/heure ne sont pas présents dans ce fichier, donc non modifiés.

### 2. Nettoyage
- Suppression de la colonne inutile `LCI Name` jugée inutile.
- Suppression des lignes contenant des valeurs manquantes (`dropna()`).
- Suppression des doublons exacts (`drop_duplicates()`).

### 3. Transformation / Enrichissement
- Aucune transformation métier ou enrichissement par jointure n’a été appliqué à ce stade.

### 4. Validation & QA
- Validation manuelle implicite via nettoyage et inspection.
- Aucun contrôle de schéma formel ni rapport de validation généré pour cette exécution.

### 5. Écriture des artéfacts traités
- Export du fichier nettoyé au format CSV vers `data/processed/`.
- Pas de fichier de métadonnées JSON généré automatiquement pour cette étape, à ajouter manuellement si nécessaire.
