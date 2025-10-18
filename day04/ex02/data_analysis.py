#!/usr/bin/env python3
"""
Exercise 02 - Analyse de Données avec Pandas
Analyse complète de données avec Pandas.
"""

import pandas as pd
import numpy as np


def creer_dataset_exemple():
    """Crée un dataset d'exemple pour l'analyse."""
    np.random.seed(42)
    
    n = 200
    
    data = {
        'Date': pd.date_range('2024-01-01', periods=n, freq='D'),
        'Produit': np.random.choice(['A', 'B', 'C', 'D'], n),
        'Region': np.random.choice(['Nord', 'Sud', 'Est', 'Ouest'], n),
        'Ventes': np.random.randint(100, 1000, n),
        'Prix': np.random.uniform(10, 100, n),
        'Quantite': np.random.randint(1, 50, n)
    }
    
    df = pd.DataFrame(data)
    df['Revenu'] = df['Ventes'] * df['Prix']
    
    return df


def analyse_exploratoire(df):
    """Effectue une analyse exploratoire des données."""
    print("=== Analyse Exploratoire ===\n")
    
    print("Aperçu des premières lignes:")
    print(df.head(10))
    print()
    
    print("Informations sur le dataset:")
    print(df.info())
    print()
    
    print("Statistiques descriptives:")
    print(df.describe())
    print()
    
    print("Valeurs uniques par colonne:")
    for col in df.columns:
        if df[col].dtype == 'object' or df[col].dtype.name == 'category':
            print(f"  {col}: {df[col].nunique()} valeurs uniques")
    print()


def analyse_par_groupe(df):
    """Analyse les données par groupes."""
    print("=== Analyse par Groupe ===\n")
    
    # Ventes par produit
    print("Ventes totales par produit:")
    ventes_produit = df.groupby('Produit')['Ventes'].agg(['sum', 'mean', 'count'])
    print(ventes_produit)
    print()
    
    # Revenu par région
    print("Revenu total par région:")
    revenu_region = df.groupby('Region')['Revenu'].sum().sort_values(ascending=False)
    print(revenu_region)
    print()
    
    # Analyse croisée
    print("Ventes moyennes par Produit et Région:")
    pivot = df.pivot_table(
        values='Ventes',
        index='Produit',
        columns='Region',
        aggfunc='mean'
    )
    print(pivot)
    print()


def analyse_temporelle(df):
    """Analyse temporelle des données."""
    print("=== Analyse Temporelle ===\n")
    
    # Définir la colonne Date comme index
    df_temp = df.set_index('Date')
    
    # Ventes par mois
    print("Ventes mensuelles:")
    ventes_mensuelles = df_temp.resample('M')['Ventes'].sum()
    print(ventes_mensuelles.head())
    print()
    
    # Moyenne mobile
    print("Moyenne mobile sur 7 jours:")
    df_temp['Ventes_MA7'] = df_temp['Ventes'].rolling(window=7).mean()
    print(df_temp[['Ventes', 'Ventes_MA7']].head(10))
    print()
    
    # Tendance
    print("Statistiques par trimestre:")
    stats_trimestre = df_temp.resample('Q')['Ventes'].agg(['sum', 'mean', 'std'])
    print(stats_trimestre)
    print()


def analyse_correlations(df):
    """Analyse les corrélations entre variables."""
    print("=== Analyse des Corrélations ===\n")
    
    # Sélectionner uniquement les colonnes numériques
    colonnes_numeriques = df.select_dtypes(include=[np.number]).columns
    
    # Matrice de corrélation
    corr_matrix = df[colonnes_numeriques].corr()
    print("Matrice de corrélation:")
    print(corr_matrix)
    print()
    
    # Identifier les corrélations fortes
    print("Corrélations fortes (|r| > 0.5):")
    for i in range(len(corr_matrix.columns)):
        for j in range(i+1, len(corr_matrix.columns)):
            if abs(corr_matrix.iloc[i, j]) > 0.5:
                print(f"  {corr_matrix.columns[i]} <-> {corr_matrix.columns[j]}: {corr_matrix.iloc[i, j]:.3f}")
    print()


def creer_nouvelles_features(df):
    """Crée de nouvelles features à partir des données existantes."""
    print("=== Création de Nouvelles Features ===\n")
    
    df_enhanced = df.copy()
    
    # Features temporelles
    df_enhanced['Jour_Semaine'] = df_enhanced['Date'].dt.day_name()
    df_enhanced['Mois'] = df_enhanced['Date'].dt.month
    df_enhanced['Trimestre'] = df_enhanced['Date'].dt.quarter
    df_enhanced['Est_Weekend'] = df_enhanced['Date'].dt.dayofweek >= 5
    
    # Features dérivées
    df_enhanced['Prix_Unitaire'] = df_enhanced['Revenu'] / df_enhanced['Quantite']
    df_enhanced['Categorie_Ventes'] = pd.cut(
        df_enhanced['Ventes'],
        bins=[0, 300, 600, 1000],
        labels=['Faible', 'Moyen', 'Élevé']
    )
    
    print("Nouvelles features créées:")
    print(df_enhanced.columns.tolist())
    print()
    
    print("Aperçu des nouvelles features:")
    print(df_enhanced[['Date', 'Jour_Semaine', 'Mois', 'Trimestre', 'Est_Weekend', 'Categorie_Ventes']].head())
    print()
    
    return df_enhanced


def rapport_complet(df):
    """Génère un rapport d'analyse complet."""
    print("="*60)
    print("RAPPORT D'ANALYSE DE DONNÉES")
    print("="*60)
    print()
    
    print(f"Période analysée: {df['Date'].min()} à {df['Date'].max()}")
    print(f"Nombre total d'observations: {len(df)}")
    print(f"Revenu total: {df['Revenu'].sum():,.2f}€")
    print(f"Ventes totales: {df['Ventes'].sum():,}")
    print()
    
    # Top produits
    print("Top 3 produits par ventes:")
    top_produits = df.groupby('Produit')['Ventes'].sum().sort_values(ascending=False).head(3)
    for produit, ventes in top_produits.items():
        print(f"  {produit}: {ventes:,} unités")
    print()
    
    # Top régions
    print("Top 3 régions par revenu:")
    top_regions = df.groupby('Region')['Revenu'].sum().sort_values(ascending=False).head(3)
    for region, revenu in top_regions.items():
        print(f"  {region}: {revenu:,.2f}€")
    print()
    
    # Statistiques clés
    print("Statistiques clés:")
    print(f"  Prix moyen: {df['Prix'].mean():.2f}€")
    print(f"  Ventes moyennes par transaction: {df['Ventes'].mean():.2f}")
    print(f"  Quantité moyenne: {df['Quantite'].mean():.2f}")
    print()


def analyse_complete():
    """Pipeline d'analyse complète."""
    print("="*60)
    print("PIPELINE D'ANALYSE COMPLÈTE")
    print("="*60)
    print()
    
    # Créer le dataset
    df = creer_dataset_exemple()
    
    # Analyses
    analyse_exploratoire(df)
    analyse_par_groupe(df)
    analyse_temporelle(df)
    analyse_correlations(df)
    df_enhanced = creer_nouvelles_features(df)
    rapport_complet(df)
    
    return df_enhanced


if __name__ == "__main__":
    df = analyse_complete()
