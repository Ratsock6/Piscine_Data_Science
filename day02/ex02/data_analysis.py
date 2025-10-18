#!/usr/bin/env python3
"""
Exercise 02 - Analyse de Données avec POO
Classes pour l'analyse de données avec programmation orientée objet.
"""

import statistics
from typing import List, Dict, Any, Optional


class Dataset:
    """
    Classe de base pour stocker et analyser des données.
    """
    
    def __init__(self, data: List[float], nom: str = "Dataset"):
        """
        Initialise un dataset.
        
        Args:
            data: Liste de valeurs numériques
            nom: Nom du dataset
        """
        self.data = data.copy()
        self.nom = nom
        self._cache = {}
    
    def moyenne(self) -> float:
        """Calcule la moyenne des données."""
        if 'moyenne' not in self._cache:
            self._cache['moyenne'] = statistics.mean(self.data)
        return self._cache['moyenne']
    
    def mediane(self) -> float:
        """Calcule la médiane des données."""
        if 'mediane' not in self._cache:
            self._cache['mediane'] = statistics.median(self.data)
        return self._cache['mediane']
    
    def ecart_type(self) -> float:
        """Calcule l'écart-type des données."""
        if 'ecart_type' not in self._cache:
            self._cache['ecart_type'] = statistics.stdev(self.data)
        return self._cache['ecart_type']
    
    def variance(self) -> float:
        """Calcule la variance des données."""
        if 'variance' not in self._cache:
            self._cache['variance'] = statistics.variance(self.data)
        return self._cache['variance']
    
    def minimum(self) -> float:
        """Retourne la valeur minimale."""
        return min(self.data)
    
    def maximum(self) -> float:
        """Retourne la valeur maximale."""
        return max(self.data)
    
    def etendue(self) -> float:
        """Retourne l'étendue (max - min)."""
        return self.maximum() - self.minimum()
    
    def quartiles(self) -> Dict[str, float]:
        """Calcule les quartiles."""
        return {
            'Q1': statistics.quantiles(self.data, n=4)[0],
            'Q2': statistics.median(self.data),
            'Q3': statistics.quantiles(self.data, n=4)[2]
        }
    
    def filtrer(self, condition) -> 'Dataset':
        """
        Filtre les données selon une condition.
        
        Args:
            condition: Fonction qui retourne True/False pour chaque valeur
        
        Returns:
            Nouveau Dataset avec les données filtrées
        """
        donnees_filtrees = [x for x in self.data if condition(x)]
        return Dataset(donnees_filtrees, f"{self.nom}_filtré")
    
    def transformer(self, fonction) -> 'Dataset':
        """
        Transforme les données avec une fonction.
        
        Args:
            fonction: Fonction à appliquer à chaque valeur
        
        Returns:
            Nouveau Dataset avec les données transformées
        """
        donnees_transformees = [fonction(x) for x in self.data]
        return Dataset(donnees_transformees, f"{self.nom}_transformé")
    
    def statistiques(self) -> Dict[str, Any]:
        """Retourne un dictionnaire de toutes les statistiques."""
        q = self.quartiles()
        return {
            'nom': self.nom,
            'nombre': len(self.data),
            'moyenne': self.moyenne(),
            'mediane': self.mediane(),
            'ecart_type': self.ecart_type(),
            'variance': self.variance(),
            'minimum': self.minimum(),
            'maximum': self.maximum(),
            'etendue': self.etendue(),
            'quartiles': q,
            'iqr': q['Q3'] - q['Q1']
        }
    
    def afficher_statistiques(self):
        """Affiche les statistiques de manière formatée."""
        stats = self.statistiques()
        print(f"\n=== Statistiques de {stats['nom']} ===")
        print(f"Nombre d'observations: {stats['nombre']}")
        print(f"Moyenne: {stats['moyenne']:.2f}")
        print(f"Médiane: {stats['mediane']:.2f}")
        print(f"Écart-type: {stats['ecart_type']:.2f}")
        print(f"Variance: {stats['variance']:.2f}")
        print(f"Minimum: {stats['minimum']:.2f}")
        print(f"Maximum: {stats['maximum']:.2f}")
        print(f"Étendue: {stats['etendue']:.2f}")
        print(f"Q1: {stats['quartiles']['Q1']:.2f}")
        print(f"Q2: {stats['quartiles']['Q2']:.2f}")
        print(f"Q3: {stats['quartiles']['Q3']:.2f}")
        print(f"IQR: {stats['iqr']:.2f}")
    
    def __len__(self):
        """Retourne le nombre d'éléments."""
        return len(self.data)
    
    def __str__(self):
        """Représentation en chaîne du dataset."""
        return f"Dataset '{self.nom}' avec {len(self.data)} observations"
    
    def __repr__(self):
        """Représentation officielle du dataset."""
        return f"Dataset(data={self.data[:5]}..., nom='{self.nom}')"


class DatasetNumerique(Dataset):
    """
    Dataset spécialisé pour les données numériques avec des analyses avancées.
    """
    
    def normaliser(self) -> 'DatasetNumerique':
        """Normalise les données entre 0 et 1."""
        min_val = self.minimum()
        max_val = self.maximum()
        etendue = max_val - min_val
        
        if etendue == 0:
            return DatasetNumerique([0] * len(self.data), f"{self.nom}_normalisé")
        
        donnees_norm = [(x - min_val) / etendue for x in self.data]
        return DatasetNumerique(donnees_norm, f"{self.nom}_normalisé")
    
    def standardiser(self) -> 'DatasetNumerique':
        """Standardise les données (z-score)."""
        moy = self.moyenne()
        std = self.ecart_type()
        
        if std == 0:
            return DatasetNumerique([0] * len(self.data), f"{self.nom}_standardisé")
        
        donnees_std = [(x - moy) / std for x in self.data]
        return DatasetNumerique(donnees_std, f"{self.nom}_standardisé")
    
    def detecter_outliers(self, methode: str = 'iqr') -> List[float]:
        """
        Détecte les outliers.
        
        Args:
            methode: 'iqr' ou 'zscore'
        
        Returns:
            Liste des outliers détectés
        """
        if methode == 'iqr':
            q = self.quartiles()
            iqr = q['Q3'] - q['Q1']
            limite_basse = q['Q1'] - 1.5 * iqr
            limite_haute = q['Q3'] + 1.5 * iqr
            return [x for x in self.data if x < limite_basse or x > limite_haute]
        
        elif methode == 'zscore':
            moy = self.moyenne()
            std = self.ecart_type()
            return [x for x in self.data if abs((x - moy) / std) > 3]
        
        return []


class DatasetCategoriel:
    """
    Dataset pour les données catégorielles.
    """
    
    def __init__(self, data: List[Any], nom: str = "Dataset Catégoriel"):
        """
        Initialise un dataset catégoriel.
        
        Args:
            data: Liste de valeurs catégorielles
            nom: Nom du dataset
        """
        self.data = data.copy()
        self.nom = nom
    
    def frequences(self) -> Dict[Any, int]:
        """Calcule les fréquences de chaque catégorie."""
        freq = {}
        for valeur in self.data:
            freq[valeur] = freq.get(valeur, 0) + 1
        return freq
    
    def proportions(self) -> Dict[Any, float]:
        """Calcule les proportions de chaque catégorie."""
        freq = self.frequences()
        total = len(self.data)
        return {k: v / total for k, v in freq.items()}
    
    def mode(self) -> Any:
        """Retourne le mode (valeur la plus fréquente)."""
        freq = self.frequences()
        return max(freq.items(), key=lambda x: x[1])[0]
    
    def nombre_categories(self) -> int:
        """Retourne le nombre de catégories uniques."""
        return len(set(self.data))
    
    def afficher_distribution(self):
        """Affiche la distribution des catégories."""
        print(f"\n=== Distribution de {self.nom} ===")
        freq = self.frequences()
        prop = self.proportions()
        
        for categorie in sorted(freq.keys()):
            print(f"{categorie}: {freq[categorie]} ({prop[categorie]*100:.1f}%)")
    
    def __len__(self):
        """Retourne le nombre d'éléments."""
        return len(self.data)
    
    def __str__(self):
        """Représentation en chaîne du dataset."""
        return f"DatasetCategoriel '{self.nom}' avec {len(self.data)} observations et {self.nombre_categories()} catégories"


# Exemple d'utilisation
if __name__ == "__main__":
    print("="*60)
    print("DÉMONSTRATION DE L'ANALYSE DE DONNÉES AVEC POO")
    print("="*60)
    
    # Dataset numérique
    donnees_num = [23, 45, 67, 12, 89, 34, 56, 78, 90, 23, 45, 67, 150]
    dataset_num = DatasetNumerique(donnees_num, "Ventes")
    
    print("\n--- Dataset Numérique ---")
    dataset_num.afficher_statistiques()
    
    # Normalisation
    print("\n--- Normalisation ---")
    dataset_norm = dataset_num.normaliser()
    print(f"Données normalisées (5 premières): {dataset_norm.data[:5]}")
    
    # Détection d'outliers
    print("\n--- Détection d'Outliers ---")
    outliers = dataset_num.detecter_outliers()
    print(f"Outliers détectés: {outliers}")
    
    # Filtrage
    print("\n--- Filtrage (valeurs > 50) ---")
    dataset_filtre = dataset_num.filtrer(lambda x: x > 50)
    print(f"Données filtrées: {dataset_filtre.data}")
    
    # Transformation
    print("\n--- Transformation (carré) ---")
    dataset_carre = dataset_num.transformer(lambda x: x ** 2)
    print(f"Données au carré (5 premières): {dataset_carre.data[:5]}")
    
    # Dataset catégoriel
    print("\n--- Dataset Catégoriel ---")
    donnees_cat = ['A', 'B', 'A', 'C', 'B', 'A', 'D', 'A', 'B', 'C']
    dataset_cat = DatasetCategoriel(donnees_cat, "Produits")
    dataset_cat.afficher_distribution()
    print(f"\nMode: {dataset_cat.mode()}")
    print(f"Nombre de catégories: {dataset_cat.nombre_categories()}")
