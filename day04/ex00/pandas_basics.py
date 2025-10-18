#!/usr/bin/env python3
"""
Exercise 00 - Introduction à Pandas
Démonstration des concepts de base de Pandas.
"""

import pandas as pd
import numpy as np


def demonstration_series():
    """Démonstration des Series Pandas."""
    print("=== Series Pandas ===\n")
    
    # Créer une Series
    s = pd.Series([1, 2, 3, 4, 5])
    print("Series simple:")
    print(s)
    print()
    
    # Series avec index personnalisé
    s_index = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
    print("Series avec index:")
    print(s_index)
    print()
    
    # Depuis un dictionnaire
    s_dict = pd.Series({'Paris': 2200000, 'Lyon': 500000, 'Marseille': 870000})
    print("Series depuis dictionnaire:")
    print(s_dict)
    print()


def demonstration_dataframe():
    """Démonstration des DataFrames."""
    print("=== DataFrames ===\n")
    
    # Créer un DataFrame depuis un dictionnaire
    data = {
        'Nom': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28],
        'Ville': ['Paris', 'Lyon', 'Marseille', 'Paris'],
        'Salaire': [35000, 42000, 38000, 45000]
    }
    df = pd.DataFrame(data)
    
    print("DataFrame:")
    print(df)
    print()
    
    print("Informations sur le DataFrame:")
    print(df.info())
    print()
    
    print("Statistiques descriptives:")
    print(df.describe())
    print()


def selection_donnees():
    """Démonstration de la sélection de données."""
    print("=== Sélection de Données ===\n")
    
    data = {
        'Nom': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 30, 35, 28, 32],
        'Ville': ['Paris', 'Lyon', 'Marseille', 'Paris', 'Lyon'],
        'Salaire': [35000, 42000, 38000, 45000, 40000]
    }
    df = pd.DataFrame(data)
    
    # Sélection de colonnes
    print("Colonne 'Nom':")
    print(df['Nom'])
    print()
    
    print("Plusieurs colonnes:")
    print(df[['Nom', 'Age']])
    print()
    
    # Sélection de lignes
    print("Premières lignes (head):")
    print(df.head(3))
    print()
    
    # Filtrage
    print("Personnes de plus de 30 ans:")
    print(df[df['Age'] > 30])
    print()
    
    print("Personnes à Paris avec salaire > 40000:")
    print(df[(df['Ville'] == 'Paris') & (df['Salaire'] > 40000)])
    print()


def manipulation_donnees():
    """Démonstration de la manipulation de données."""
    print("=== Manipulation de Données ===\n")
    
    data = {
        'Nom': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Salaire': [35000, 42000, 38000]
    }
    df = pd.DataFrame(data)
    
    print("DataFrame original:")
    print(df)
    print()
    
    # Ajouter une colonne
    df['Bonus'] = df['Salaire'] * 0.1
    print("Après ajout de la colonne Bonus:")
    print(df)
    print()
    
    # Modifier une colonne
    df['Age'] = df['Age'] + 1
    print("Après vieillissement d'un an:")
    print(df)
    print()
    
    # Supprimer une colonne
    df_sans_bonus = df.drop('Bonus', axis=1)
    print("Après suppression de Bonus:")
    print(df_sans_bonus)
    print()


def operations_groupement():
    """Démonstration des opérations de groupement."""
    print("=== Groupement et Agrégation ===\n")
    
    data = {
        'Ville': ['Paris', 'Lyon', 'Paris', 'Lyon', 'Marseille', 'Paris'],
        'Categorie': ['A', 'A', 'B', 'B', 'A', 'B'],
        'Ventes': [100, 150, 200, 180, 120, 160]
    }
    df = pd.DataFrame(data)
    
    print("DataFrame:")
    print(df)
    print()
    
    # Groupement par ville
    print("Ventes par ville:")
    print(df.groupby('Ville')['Ventes'].sum())
    print()
    
    # Groupement multiple
    print("Ventes par ville et catégorie:")
    print(df.groupby(['Ville', 'Categorie'])['Ventes'].sum())
    print()
    
    # Agrégations multiples
    print("Statistiques par ville:")
    print(df.groupby('Ville')['Ventes'].agg(['sum', 'mean', 'count']))
    print()


if __name__ == "__main__":
    demonstration_series()
    demonstration_dataframe()
    selection_donnees()
    manipulation_donnees()
    operations_groupement()
