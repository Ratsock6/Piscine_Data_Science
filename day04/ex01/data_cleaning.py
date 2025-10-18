#!/usr/bin/env python3
"""
Exercise 01 - Nettoyage de Données
Techniques de nettoyage et préparation des données avec Pandas.
"""

import pandas as pd
import numpy as np


def creer_donnees_exemple():
    """Crée un DataFrame avec des données sales pour la démonstration."""
    data = {
        'Nom': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Bob', None, 'Frank'],
        'Age': [25, 30, None, 28, 32, 30, 27, 150],  # 150 est un outlier
        'Ville': ['Paris', 'Lyon', 'Marseille', 'Paris', None, 'Lyon', 'Nice', 'paris'],
        'Salaire': [35000, 42000, None, 45000, 40000, 42000, 38000, 35000],
        'Score': [85.5, 90.0, 78.5, None, 88.0, 90.0, 82.5, 95.0]
    }
    return pd.DataFrame(data)


def analyser_donnees(df):
    """Analyse les problèmes dans les données."""
    print("=== Analyse des Données ===\n")
    
    print("Aperçu des données:")
    print(df)
    print()
    
    print("Informations sur le DataFrame:")
    print(df.info())
    print()
    
    print("Valeurs manquantes par colonne:")
    print(df.isnull().sum())
    print()
    
    print("Nombre de doublons:", df.duplicated().sum())
    print()


def gerer_valeurs_manquantes(df):
    """Gère les valeurs manquantes."""
    print("=== Gestion des Valeurs Manquantes ===\n")
    
    df_clean = df.copy()
    
    # Remplir les valeurs manquantes de 'Age' avec la moyenne
    age_moyenne = df_clean['Age'].mean()
    df_clean['Age'].fillna(age_moyenne, inplace=True)
    print(f"Age manquant remplacé par la moyenne: {age_moyenne:.2f}")
    
    # Remplir les valeurs manquantes de 'Ville' avec 'Inconnue'
    df_clean['Ville'].fillna('Inconnue', inplace=True)
    print("Ville manquante remplacée par 'Inconnue'")
    
    # Remplir les valeurs manquantes de 'Salaire' avec la médiane
    salaire_median = df_clean['Salaire'].median()
    df_clean['Salaire'].fillna(salaire_median, inplace=True)
    print(f"Salaire manquant remplacé par la médiane: {salaire_median}")
    
    # Remplir les valeurs manquantes de 'Score' par interpolation
    df_clean['Score'].interpolate(method='linear', inplace=True)
    print("Score manquant remplacé par interpolation")
    
    # Supprimer les lignes avec des noms manquants
    df_clean.dropna(subset=['Nom'], inplace=True)
    print("Lignes avec Nom manquant supprimées")
    
    print("\nDonnées après traitement des valeurs manquantes:")
    print(df_clean)
    print()
    
    return df_clean


def supprimer_doublons(df):
    """Supprime les doublons."""
    print("=== Suppression des Doublons ===\n")
    
    print(f"Nombre de lignes avant: {len(df)}")
    df_clean = df.drop_duplicates()
    print(f"Nombre de lignes après: {len(df_clean)}")
    print(f"Doublons supprimés: {len(df) - len(df_clean)}")
    print()
    
    return df_clean


def normaliser_donnees(df):
    """Normalise les données textuelles."""
    print("=== Normalisation des Données ===\n")
    
    df_clean = df.copy()
    
    # Normaliser les noms de villes (mettre en majuscules la première lettre)
    df_clean['Ville'] = df_clean['Ville'].str.capitalize()
    print("Villes normalisées (première lettre en majuscule)")
    
    # Normaliser les noms (supprimer les espaces inutiles)
    df_clean['Nom'] = df_clean['Nom'].str.strip()
    print("Noms normalisés (espaces supprimés)")
    
    print("\nDonnées après normalisation:")
    print(df_clean)
    print()
    
    return df_clean


def detecter_outliers(df, colonne):
    """Détecte les outliers en utilisant l'IQR."""
    print(f"=== Détection des Outliers pour '{colonne}' ===\n")
    
    Q1 = df[colonne].quantile(0.25)
    Q3 = df[colonne].quantile(0.75)
    IQR = Q3 - Q1
    
    limite_basse = Q1 - 1.5 * IQR
    limite_haute = Q3 + 1.5 * IQR
    
    print(f"Q1: {Q1}, Q3: {Q3}, IQR: {IQR}")
    print(f"Limites: [{limite_basse}, {limite_haute}]")
    
    outliers = df[(df[colonne] < limite_basse) | (df[colonne] > limite_haute)]
    
    if len(outliers) > 0:
        print(f"\nOutliers détectés ({len(outliers)}):")
        print(outliers[[colonne]])
    else:
        print("\nAucun outlier détecté")
    
    print()
    
    return outliers


def traiter_outliers(df, colonne, methode='cap'):
    """Traite les outliers."""
    print(f"=== Traitement des Outliers pour '{colonne}' ===\n")
    
    df_clean = df.copy()
    
    Q1 = df_clean[colonne].quantile(0.25)
    Q3 = df_clean[colonne].quantile(0.75)
    IQR = Q3 - Q1
    
    limite_basse = Q1 - 1.5 * IQR
    limite_haute = Q3 + 1.5 * IQR
    
    if methode == 'cap':
        # Plafonner les valeurs
        df_clean[colonne] = df_clean[colonne].clip(lower=limite_basse, upper=limite_haute)
        print(f"Outliers plafonnés à [{limite_basse}, {limite_haute}]")
    elif methode == 'remove':
        # Supprimer les lignes avec outliers
        df_clean = df_clean[(df_clean[colonne] >= limite_basse) & (df_clean[colonne] <= limite_haute)]
        print(f"Lignes avec outliers supprimées")
    
    print(f"\nDonnées après traitement:")
    print(df_clean)
    print()
    
    return df_clean


def pipeline_nettoyage():
    """Pipeline complet de nettoyage des données."""
    print("="*60)
    print("PIPELINE DE NETTOYAGE DE DONNÉES")
    print("="*60)
    print()
    
    # Étape 1: Créer les données
    df = creer_donnees_exemple()
    
    # Étape 2: Analyser
    analyser_donnees(df)
    
    # Étape 3: Gérer les valeurs manquantes
    df = gerer_valeurs_manquantes(df)
    
    # Étape 4: Supprimer les doublons
    df = supprimer_doublons(df)
    
    # Étape 5: Normaliser
    df = normaliser_donnees(df)
    
    # Étape 6: Détecter et traiter les outliers
    detecter_outliers(df, 'Age')
    df = traiter_outliers(df, 'Age', methode='cap')
    
    # Résultat final
    print("="*60)
    print("DONNÉES NETTOYÉES FINALES")
    print("="*60)
    print(df)
    print()
    
    print("Statistiques des données nettoyées:")
    print(df.describe())
    
    return df


if __name__ == "__main__":
    df_propre = pipeline_nettoyage()
