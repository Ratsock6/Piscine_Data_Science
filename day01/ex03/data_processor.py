#!/usr/bin/env python3
"""
Exercise 03 - Module de Traitement de Données
Module pour traiter et analyser des listes de données.
"""


def lire_nombres(fichier):
    """
    Lit des nombres depuis un fichier (un nombre par ligne).
    
    Args:
        fichier: Chemin du fichier à lire
    
    Returns:
        Liste de nombres
    
    Raises:
        FileNotFoundError: Si le fichier n'existe pas
        ValueError: Si le fichier contient des données invalides
    """
    nombres = []
    try:
        with open(fichier, 'r') as f:
            for ligne_num, ligne in enumerate(f, 1):
                ligne = ligne.strip()
                if ligne:  # Ignorer les lignes vides
                    try:
                        nombres.append(float(ligne))
                    except ValueError:
                        raise ValueError(f"Ligne {ligne_num}: '{ligne}' n'est pas un nombre valide")
    except FileNotFoundError:
        raise FileNotFoundError(f"Le fichier '{fichier}' n'existe pas")
    
    return nombres


def filtrer_pairs(liste):
    """
    Retourne uniquement les nombres pairs d'une liste.
    
    Args:
        liste: Liste de nombres
    
    Returns:
        Liste contenant uniquement les nombres pairs
    """
    return [x for x in liste if x % 2 == 0]


def filtrer_impairs(liste):
    """
    Retourne uniquement les nombres impairs d'une liste.
    
    Args:
        liste: Liste de nombres
    
    Returns:
        Liste contenant uniquement les nombres impairs
    """
    return [x for x in liste if x % 2 != 0]


def appliquer_fonction(liste, fonction):
    """
    Applique une fonction à chaque élément d'une liste.
    
    Args:
        liste: Liste d'éléments
        fonction: Fonction à appliquer (doit accepter un argument)
    
    Returns:
        Liste avec la fonction appliquée à chaque élément
    """
    return [fonction(x) for x in liste]


def filtrer_par_condition(liste, condition):
    """
    Filtre une liste selon une condition.
    
    Args:
        liste: Liste d'éléments
        condition: Fonction qui retourne True ou False
    
    Returns:
        Liste filtrée
    """
    return [x for x in liste if condition(x)]


def transformer_donnees(liste, transformations):
    """
    Applique plusieurs transformations successives à une liste.
    
    Args:
        liste: Liste de données
        transformations: Liste de fonctions à appliquer
    
    Returns:
        Liste transformée
    """
    resultat = liste
    for transformation in transformations:
        resultat = appliquer_fonction(resultat, transformation)
    return resultat


# Exemple d'utilisation
if __name__ == "__main__":
    print("Démonstration du module de traitement de données:\n")
    
    # Données d'exemple
    nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Liste originale: {nombres}")
    
    # Filtrer les pairs et impairs
    pairs = filtrer_pairs(nombres)
    impairs = filtrer_impairs(nombres)
    print(f"\nNombres pairs: {pairs}")
    print(f"Nombres impairs: {impairs}")
    
    # Appliquer une fonction (carré)
    carres = appliquer_fonction(nombres, lambda x: x ** 2)
    print(f"\nCarrés: {carres}")
    
    # Filtrer par condition personnalisée (nombres > 5)
    grands = filtrer_par_condition(nombres, lambda x: x > 5)
    print(f"\nNombres > 5: {grands}")
    
    # Transformations multiples
    transformations = [
        lambda x: x * 2,      # Doubler
        lambda x: x + 1,      # Ajouter 1
        lambda x: x ** 2      # Carré
    ]
    transformes = transformer_donnees([1, 2, 3], transformations)
    print(f"\nTransformations multiples sur [1, 2, 3]:")
    print(f"  (x * 2 + 1) ** 2 = {transformes}")
