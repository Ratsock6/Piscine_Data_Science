#!/usr/bin/env python3
"""
Exercise 01 - Visualisations Avancées avec Seaborn
Création de visualisations statistiques avec Seaborn.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd


def creer_dataset():
    """Crée un dataset pour les visualisations."""
    np.random.seed(42)
    
    n = 200
    
    data = {
        'Categorie': np.random.choice(['A', 'B', 'C'], n),
        'Valeur': np.random.randn(n) * 15 + 50,
        'Groupe': np.random.choice(['Groupe 1', 'Groupe 2', 'Groupe 3'], n),
        'Score': np.random.uniform(0, 100, n),
        'Age': np.random.randint(18, 65, n)
    }
    
    df = pd.DataFrame(data)
    df['Valeur2'] = df['Valeur'] + np.random.randn(n) * 5
    
    return df


def heatmap_correlation():
    """Crée une heatmap de corrélation."""
    print("Création de la heatmap de corrélation...")
    
    # Générer des données corrélées
    np.random.seed(42)
    n = 100
    data = {
        'Variable_A': np.random.randn(n),
        'Variable_B': np.random.randn(n),
        'Variable_C': np.random.randn(n),
        'Variable_D': np.random.randn(n)
    }
    
    # Ajouter des corrélations
    data['Variable_B'] = data['Variable_A'] * 0.8 + np.random.randn(n) * 0.5
    data['Variable_C'] = data['Variable_A'] * -0.6 + np.random.randn(n) * 0.5
    
    df = pd.DataFrame(data)
    
    # Calculer la matrice de corrélation
    corr = df.corr()
    
    # Créer la heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', center=0,
                square=True, linewidths=1, cbar_kws={"shrink": 0.8})
    plt.title('Heatmap de Corrélation', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig('/tmp/heatmap.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("  Sauvegardé: /tmp/heatmap.png")


def violin_plot():
    """Crée des violin plots."""
    print("Création des violin plots...")
    
    df = creer_dataset()
    
    plt.figure(figsize=(12, 6))
    sns.violinplot(data=df, x='Categorie', y='Valeur', hue='Groupe',
                   split=False, palette='Set2')
    plt.title('Distribution des Valeurs par Catégorie et Groupe', fontsize=14, fontweight='bold')
    plt.xlabel('Catégorie', fontsize=12)
    plt.ylabel('Valeur', fontsize=12)
    plt.legend(title='Groupe')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('/tmp/violin_plot.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("  Sauvegardé: /tmp/violin_plot.png")


def pair_plot():
    """Crée un pair plot."""
    print("Création du pair plot...")
    
    df = creer_dataset()
    
    # Sélectionner les colonnes numériques
    df_numeric = df[['Valeur', 'Valeur2', 'Score', 'Age', 'Categorie']]
    
    # Créer le pair plot
    g = sns.pairplot(df_numeric, hue='Categorie', palette='husl',
                     diag_kind='kde', plot_kws={'alpha': 0.6})
    g.fig.suptitle('Pair Plot - Relations entre Variables', y=1.02, fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig('/tmp/pair_plot.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("  Sauvegardé: /tmp/pair_plot.png")


def distribution_plots():
    """Crée des graphiques de distribution."""
    print("Création des graphiques de distribution...")
    
    df = creer_dataset()
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # Distribution plot
    sns.histplot(data=df, x='Valeur', kde=True, ax=axes[0, 0], color='skyblue')
    axes[0, 0].set_title('Histogramme avec KDE', fontweight='bold')
    axes[0, 0].grid(True, alpha=0.3)
    
    # Box plot
    sns.boxplot(data=df, x='Categorie', y='Score', ax=axes[0, 1], palette='Set3')
    axes[0, 1].set_title('Box Plot par Catégorie', fontweight='bold')
    axes[0, 1].grid(True, alpha=0.3)
    
    # KDE plot
    for cat in df['Categorie'].unique():
        subset = df[df['Categorie'] == cat]
        sns.kdeplot(data=subset, x='Valeur', ax=axes[1, 0], label=cat, fill=True, alpha=0.5)
    axes[1, 0].set_title('KDE Plot par Catégorie', fontweight='bold')
    axes[1, 0].legend()
    axes[1, 0].grid(True, alpha=0.3)
    
    # Swarm plot
    sns.swarmplot(data=df.sample(50), x='Categorie', y='Score', hue='Groupe',
                  ax=axes[1, 1], palette='deep')
    axes[1, 1].set_title('Swarm Plot (échantillon)', fontweight='bold')
    axes[1, 1].grid(True, alpha=0.3)
    axes[1, 1].legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    
    plt.tight_layout()
    plt.savefig('/tmp/distributions.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("  Sauvegardé: /tmp/distributions.png")


def regression_plot():
    """Crée un graphique de régression."""
    print("Création du graphique de régression...")
    
    df = creer_dataset()
    
    plt.figure(figsize=(12, 6))
    
    # Régression linéaire avec intervalle de confiance
    sns.regplot(data=df, x='Valeur', y='Valeur2', scatter_kws={'alpha': 0.5},
                line_kws={'color': 'red', 'linewidth': 2})
    
    plt.title('Régression Linéaire avec Intervalle de Confiance',
              fontsize=14, fontweight='bold')
    plt.xlabel('Valeur', fontsize=12)
    plt.ylabel('Valeur 2', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('/tmp/regression.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("  Sauvegardé: /tmp/regression.png")


def creer_toutes_visualisations():
    """Crée toutes les visualisations Seaborn."""
    print("="*60)
    print("CRÉATION DES VISUALISATIONS SEABORN")
    print("="*60)
    print()
    
    # Configurer le style Seaborn
    sns.set_style("whitegrid")
    sns.set_context("notebook")
    
    heatmap_correlation()
    violin_plot()
    pair_plot()
    distribution_plots()
    regression_plot()
    
    print()
    print("Toutes les visualisations ont été créées avec succès!")


if __name__ == "__main__":
    creer_toutes_visualisations()
