#!/usr/bin/env python3
"""
Exercise 02 - Analyse Statistique avec NumPy
Application de NumPy pour l'analyse statistique.
"""

import numpy as np


def generer_donnees():
    """Génère des données aléatoires pour l'analyse."""
    np.random.seed(42)  # Pour la reproductibilité
    
    # Générer différents types de distributions
    normale = np.random.normal(100, 15, 1000)
    uniforme = np.random.uniform(0, 100, 1000)
    exponentielle = np.random.exponential(2, 1000)
    
    return normale, uniforme, exponentielle


def statistiques_descriptives(data, nom="Dataset"):
    """Calcule les statistiques descriptives."""
    print(f"=== Statistiques pour {nom} ===")
    print(f"Nombre d'observations: {len(data)}")
    print(f"Moyenne: {np.mean(data):.2f}")
    print(f"Médiane: {np.median(data):.2f}")
    print(f"Écart-type: {np.std(data):.2f}")
    print(f"Variance: {np.var(data):.2f}")
    print(f"Minimum: {np.min(data):.2f}")
    print(f"Maximum: {np.max(data):.2f}")
    print(f"Étendue: {np.ptp(data):.2f}")
    
    # Quartiles
    q25, q50, q75 = np.percentile(data, [25, 50, 75])
    print(f"\nQuartiles:")
    print(f"  Q1 (25%): {q25:.2f}")
    print(f"  Q2 (50%): {q50:.2f}")
    print(f"  Q3 (75%): {q75:.2f}")
    print(f"  IQR: {q75 - q25:.2f}")
    print()


def correlation_covariance():
    """Calcule corrélation et covariance."""
    print("=== Corrélation et Covariance ===\n")
    
    # Générer deux variables corrélées
    x = np.random.randn(100)
    y = 2 * x + np.random.randn(100) * 0.5
    z = np.random.randn(100)  # Variable indépendante
    
    # Créer une matrice de données
    data = np.vstack([x, y, z])
    
    # Matrice de covariance
    cov_matrix = np.cov(data)
    print("Matrice de covariance:")
    print(cov_matrix)
    print()
    
    # Matrice de corrélation
    corr_matrix = np.corrcoef(data)
    print("Matrice de corrélation:")
    print(corr_matrix)
    print()
    
    print(f"Corrélation entre x et y: {np.corrcoef(x, y)[0, 1]:.3f}")
    print(f"Corrélation entre x et z: {np.corrcoef(x, z)[0, 1]:.3f}")
    print()


def transformations_donnees():
    """Applique des transformations aux données."""
    print("=== Transformations de Données ===\n")
    
    data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(f"Données originales: {data}\n")
    
    # Normalisation (0-1)
    data_norm = (data - np.min(data)) / (np.max(data) - np.min(data))
    print(f"Normalisation (0-1): {data_norm}")
    
    # Standardisation (z-score)
    data_std = (data - np.mean(data)) / np.std(data)
    print(f"Standardisation: {data_std}")
    
    # Transformation logarithmique
    data_log = np.log(data)
    print(f"Log transformation: {data_log}")
    
    # Transformation racine carrée
    data_sqrt = np.sqrt(data)
    print(f"Sqrt transformation: {data_sqrt}")
    print()


def echantillonnage():
    """Démonstration de l'échantillonnage."""
    print("=== Échantillonnage ===\n")
    
    population = np.arange(1, 101)
    
    # Échantillonnage aléatoire simple
    echantillon = np.random.choice(population, size=10, replace=False)
    print(f"Échantillon aléatoire (n=10): {sorted(echantillon)}")
    
    # Échantillonnage avec remplacement
    echantillon_replace = np.random.choice(population, size=10, replace=True)
    print(f"Échantillonnage avec remplacement: {sorted(echantillon_replace)}")
    
    # Échantillonnage stratifié simple
    n_strates = 5
    taille_strate = len(population) // n_strates
    echantillon_stratifie = []
    
    for i in range(n_strates):
        strate = population[i*taille_strate:(i+1)*taille_strate]
        echantillon_stratifie.extend(np.random.choice(strate, size=2, replace=False))
    
    print(f"Échantillonnage stratifié: {sorted(echantillon_stratifie)}")
    print()


def tests_hypotheses_simple():
    """Démonstration simple de tests d'hypothèses."""
    print("=== Tests d'Hypothèses Simples ===\n")
    
    # Générer deux échantillons
    np.random.seed(42)
    echantillon1 = np.random.normal(100, 15, 100)
    echantillon2 = np.random.normal(105, 15, 100)
    
    print("Échantillon 1:")
    print(f"  Moyenne: {np.mean(echantillon1):.2f}")
    print(f"  Écart-type: {np.std(echantillon1):.2f}")
    
    print("\nÉchantillon 2:")
    print(f"  Moyenne: {np.mean(echantillon2):.2f}")
    print(f"  Écart-type: {np.std(echantillon2):.2f}")
    
    print(f"\nDifférence des moyennes: {np.mean(echantillon2) - np.mean(echantillon1):.2f}")
    print()


def analyse_complete():
    """Analyse statistique complète."""
    print("="*60)
    print("ANALYSE STATISTIQUE COMPLÈTE")
    print("="*60)
    print()
    
    # Générer les données
    normale, uniforme, exponentielle = generer_donnees()
    
    # Analyser chaque distribution
    statistiques_descriptives(normale, "Distribution Normale")
    statistiques_descriptives(uniforme, "Distribution Uniforme")
    statistiques_descriptives(exponentielle, "Distribution Exponentielle")
    
    # Autres analyses
    correlation_covariance()
    transformations_donnees()
    echantillonnage()
    tests_hypotheses_simple()


if __name__ == "__main__":
    analyse_complete()
