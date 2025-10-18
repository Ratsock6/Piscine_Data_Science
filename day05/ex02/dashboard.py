#!/usr/bin/env python3
"""
Exercise 02 - Tableau de Bord
Création d'un tableau de bord complet avec plusieurs visualisations.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from datetime import datetime, timedelta


def generer_donnees_ventes():
    """Génère des données de ventes pour le tableau de bord."""
    np.random.seed(42)
    
    # Dates sur 12 mois
    dates = pd.date_range(start='2024-01-01', periods=365, freq='D')
    
    n = len(dates)
    
    # Générer des données avec tendance et saisonnalité
    tendance = np.linspace(1000, 1500, n)
    saisonnalite = 200 * np.sin(np.arange(n) * 2 * np.pi / 365)
    bruit = np.random.randn(n) * 50
    
    ventes = tendance + saisonnalite + bruit
    
    data = {
        'Date': dates,
        'Ventes': ventes,
        'Produit': np.random.choice(['Produit A', 'Produit B', 'Produit C'], n),
        'Region': np.random.choice(['Nord', 'Sud', 'Est', 'Ouest'], n),
        'Client_Type': np.random.choice(['Nouveau', 'Fidèle'], n, p=[0.3, 0.7]),
        'Prix_Unitaire': np.random.uniform(10, 100, n),
        'Quantite': np.random.randint(1, 20, n)
    }
    
    df = pd.DataFrame(data)
    df['Revenu'] = df['Prix_Unitaire'] * df['Quantite']
    df['Mois'] = df['Date'].dt.to_period('M')
    
    return df


def creer_dashboard(df):
    """Crée un tableau de bord complet."""
    print("Création du tableau de bord...")
    
    # Configuration du style
    sns.set_style("whitegrid")
    plt.style.use('seaborn-v0_8-darkgrid')
    
    # Créer la figure avec subplots
    fig = plt.figure(figsize=(20, 12))
    gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)
    
    # Couleurs personnalisées
    colors = sns.color_palette("husl", 8)
    
    # 1. Évolution des ventes dans le temps
    ax1 = fig.add_subplot(gs[0, :])
    ventes_mensuelles = df.groupby('Mois')['Ventes'].sum()
    ax1.plot(range(len(ventes_mensuelles)), ventes_mensuelles.values,
             marker='o', linewidth=2, markersize=6, color=colors[0])
    ax1.fill_between(range(len(ventes_mensuelles)), ventes_mensuelles.values,
                      alpha=0.3, color=colors[0])
    ax1.set_title('Évolution des Ventes Mensuelles', fontsize=14, fontweight='bold', pad=20)
    ax1.set_xlabel('Mois', fontsize=11)
    ax1.set_ylabel('Ventes (€)', fontsize=11)
    ax1.grid(True, alpha=0.3)
    ax1.set_xticks(range(len(ventes_mensuelles)))
    ax1.set_xticklabels([str(m) for m in ventes_mensuelles.index], rotation=45)
    
    # 2. Ventes par produit (camembert)
    ax2 = fig.add_subplot(gs[1, 0])
    ventes_produit = df.groupby('Produit')['Revenu'].sum()
    ax2.pie(ventes_produit.values, labels=ventes_produit.index,
            autopct='%1.1f%%', startangle=90, colors=colors[1:4])
    ax2.set_title('Répartition des Revenus par Produit', fontsize=12, fontweight='bold', pad=20)
    
    # 3. Ventes par région (barres)
    ax3 = fig.add_subplot(gs[1, 1])
    ventes_region = df.groupby('Region')['Revenu'].sum().sort_values(ascending=False)
    ax3.bar(ventes_region.index, ventes_region.values, color=colors[4:], edgecolor='black')
    ax3.set_title('Revenus par Région', fontsize=12, fontweight='bold', pad=20)
    ax3.set_ylabel('Revenu (€)', fontsize=11)
    ax3.grid(True, alpha=0.3, axis='y')
    ax3.tick_params(axis='x', rotation=45)
    
    # 4. Distribution des prix (histogramme)
    ax4 = fig.add_subplot(gs[1, 2])
    ax4.hist(df['Prix_Unitaire'], bins=30, color=colors[5], edgecolor='black', alpha=0.7)
    ax4.set_title('Distribution des Prix Unitaires', fontsize=12, fontweight='bold', pad=20)
    ax4.set_xlabel('Prix (€)', fontsize=11)
    ax4.set_ylabel('Fréquence', fontsize=11)
    ax4.grid(True, alpha=0.3)
    
    # 5. Comparaison nouveaux vs fidèles (box plot)
    ax5 = fig.add_subplot(gs[2, 0])
    df.boxplot(column='Revenu', by='Client_Type', ax=ax5,
               patch_artist=True, boxprops=dict(facecolor=colors[6]))
    ax5.set_title('Revenus par Type de Client', fontsize=12, fontweight='bold', pad=20)
    ax5.set_xlabel('Type de Client', fontsize=11)
    ax5.set_ylabel('Revenu (€)', fontsize=11)
    plt.sca(ax5)
    plt.xticks([1, 2], ['Fidèle', 'Nouveau'])
    ax5.get_figure().suptitle('')  # Supprimer le titre automatique
    
    # 6. Top 10 jours de ventes (barres horizontales)
    ax6 = fig.add_subplot(gs[2, 1])
    ventes_journalieres = df.groupby('Date')['Revenu'].sum().sort_values(ascending=False).head(10)
    y_pos = np.arange(len(ventes_journalieres))
    ax6.barh(y_pos, ventes_journalieres.values, color=colors[7], edgecolor='black')
    ax6.set_yticks(y_pos)
    ax6.set_yticklabels([d.strftime('%d/%m') for d in ventes_journalieres.index], fontsize=9)
    ax6.set_title('Top 10 Meilleurs Jours', fontsize=12, fontweight='bold', pad=20)
    ax6.set_xlabel('Revenu (€)', fontsize=11)
    ax6.grid(True, alpha=0.3, axis='x')
    ax6.invert_yaxis()
    
    # 7. Statistiques clés (texte)
    ax7 = fig.add_subplot(gs[2, 2])
    ax7.axis('off')
    
    stats_text = f"""
    STATISTIQUES CLÉS
    {'='*30}
    
    Revenu Total: {df['Revenu'].sum():,.0f} €
    
    Ventes Moyennes: {df['Ventes'].mean():.2f} €
    
    Nombre de Transactions: {len(df):,}
    
    Prix Moyen: {df['Prix_Unitaire'].mean():.2f} €
    
    Quantité Moyenne: {df['Quantite'].mean():.1f}
    
    Meilleur Produit: {df.groupby('Produit')['Revenu'].sum().idxmax()}
    
    Meilleure Région: {df.groupby('Region')['Revenu'].sum().idxmax()}
    """
    
    ax7.text(0.1, 0.5, stats_text, fontsize=11, family='monospace',
             verticalalignment='center', bbox=dict(boxstyle='round',
             facecolor='wheat', alpha=0.5))
    
    # Titre général
    fig.suptitle('TABLEAU DE BORD - ANALYSE DES VENTES 2024',
                 fontsize=18, fontweight='bold', y=0.98)
    
    # Sauvegarder
    plt.savefig('/tmp/dashboard.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("  Tableau de bord sauvegardé: /tmp/dashboard.png")


def creer_dashboard_simple(df):
    """Crée un tableau de bord simplifié."""
    print("Création du tableau de bord simplifié...")
    
    fig, axes = plt.subplots(2, 2, figsize=(16, 10))
    fig.suptitle('Tableau de Bord Simplifié', fontsize=16, fontweight='bold')
    
    # 1. Tendance temporelle
    ventes_mensuelles = df.groupby('Mois')['Ventes'].sum()
    axes[0, 0].plot(range(len(ventes_mensuelles)), ventes_mensuelles.values, marker='o')
    axes[0, 0].set_title('Ventes Mensuelles')
    axes[0, 0].grid(True, alpha=0.3)
    
    # 2. Ventes par produit
    ventes_produit = df.groupby('Produit')['Revenu'].sum()
    axes[0, 1].bar(ventes_produit.index, ventes_produit.values)
    axes[0, 1].set_title('Revenus par Produit')
    axes[0, 1].grid(True, alpha=0.3, axis='y')
    
    # 3. Distribution
    axes[1, 0].hist(df['Prix_Unitaire'], bins=20, edgecolor='black')
    axes[1, 0].set_title('Distribution des Prix')
    axes[1, 0].grid(True, alpha=0.3)
    
    # 4. Scatter plot
    axes[1, 1].scatter(df['Quantite'], df['Revenu'], alpha=0.5)
    axes[1, 1].set_title('Quantité vs Revenu')
    axes[1, 1].set_xlabel('Quantité')
    axes[1, 1].set_ylabel('Revenu')
    axes[1, 1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/tmp/dashboard_simple.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("  Tableau de bord simplifié sauvegardé: /tmp/dashboard_simple.png")


if __name__ == "__main__":
    print("="*60)
    print("CRÉATION DU TABLEAU DE BORD")
    print("="*60)
    print()
    
    # Générer les données
    df = generer_donnees_ventes()
    
    # Créer les tableaux de bord
    creer_dashboard(df)
    creer_dashboard_simple(df)
    
    print()
    print("Tous les tableaux de bord ont été créés avec succès!")
