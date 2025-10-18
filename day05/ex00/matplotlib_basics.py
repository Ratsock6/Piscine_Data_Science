#!/usr/bin/env python3
"""
Exercise 00 - Graphiques de Base avec Matplotlib
Démonstration des différents types de graphiques.
"""

import matplotlib.pyplot as plt
import numpy as np


def graphique_lineaire():
    """Crée un graphique linéaire simple."""
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y1, label='sin(x)', linewidth=2)
    plt.plot(x, y2, label='cos(x)', linewidth=2, linestyle='--')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Fonctions Trigonométriques')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('/tmp/graphique_lineaire.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Graphique linéaire sauvegardé: /tmp/graphique_lineaire.png")


def histogramme():
    """Crée un histogramme."""
    # Générer des données aléatoires
    data = np.random.randn(1000)
    
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=30, edgecolor='black', alpha=0.7)
    plt.xlabel('Valeur')
    plt.ylabel('Fréquence')
    plt.title('Distribution Normale')
    plt.grid(True, alpha=0.3)
    plt.savefig('/tmp/histogramme.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Histogramme sauvegardé: /tmp/histogramme.png")


def diagramme_barres():
    """Crée un diagramme en barres."""
    categories = ['A', 'B', 'C', 'D', 'E']
    valeurs = [23, 45, 56, 78, 32]
    
    plt.figure(figsize=(10, 6))
    plt.bar(categories, valeurs, color='skyblue', edgecolor='black')
    plt.xlabel('Catégories')
    plt.ylabel('Valeurs')
    plt.title('Diagramme en Barres')
    plt.grid(True, alpha=0.3, axis='y')
    plt.savefig('/tmp/diagramme_barres.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Diagramme en barres sauvegardé: /tmp/diagramme_barres.png")


def scatter_plot():
    """Crée un scatter plot."""
    n = 100
    x = np.random.randn(n)
    y = 2 * x + np.random.randn(n) * 0.5
    colors = np.random.rand(n)
    sizes = 1000 * np.random.rand(n)
    
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, c=colors, s=sizes, alpha=0.6, cmap='viridis')
    plt.colorbar(label='Couleur')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Scatter Plot avec Couleurs et Tailles Variables')
    plt.grid(True, alpha=0.3)
    plt.savefig('/tmp/scatter_plot.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Scatter plot sauvegardé: /tmp/scatter_plot.png")


def subplots_exemple():
    """Crée plusieurs graphiques dans une figure."""
    x = np.linspace(0, 10, 100)
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Graphique 1
    axes[0, 0].plot(x, np.sin(x))
    axes[0, 0].set_title('sin(x)')
    axes[0, 0].grid(True, alpha=0.3)
    
    # Graphique 2
    axes[0, 1].plot(x, np.cos(x), 'r')
    axes[0, 1].set_title('cos(x)')
    axes[0, 1].grid(True, alpha=0.3)
    
    # Graphique 3
    axes[1, 0].plot(x, x**2, 'g')
    axes[1, 0].set_title('x²')
    axes[1, 0].grid(True, alpha=0.3)
    
    # Graphique 4
    axes[1, 1].plot(x, np.exp(-x), 'orange')
    axes[1, 1].set_title('e^(-x)')
    axes[1, 1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/tmp/subplots.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Subplots sauvegardés: /tmp/subplots.png")


if __name__ == "__main__":
    print("Création des graphiques...\n")
    graphique_lineaire()
    histogramme()
    diagramme_barres()
    scatter_plot()
    subplots_exemple()
    print("\nTous les graphiques ont été créés avec succès!")
