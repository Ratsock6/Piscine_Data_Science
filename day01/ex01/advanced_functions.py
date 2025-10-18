#!/usr/bin/env python3
"""
Exercise 01 - Fonctions avec Paramètres Variables
Module contenant des fonctions avec *args et **kwargs.
"""


def somme(*args):
    """
    Retourne la somme de tous les arguments.
    
    Args:
        *args: Nombres à additionner
    
    Returns:
        La somme de tous les arguments
    """
    return sum(args)


def moyenne(*args):
    """
    Retourne la moyenne des arguments.
    
    Args:
        *args: Nombres dont on veut la moyenne
    
    Returns:
        La moyenne des arguments, ou 0 si aucun argument
    """
    if len(args) == 0:
        return 0
    return sum(args) / len(args)


def minimum(*args):
    """
    Retourne le minimum des arguments.
    
    Args:
        *args: Nombres à comparer
    
    Returns:
        Le minimum des arguments
    
    Raises:
        ValueError: Si aucun argument n'est fourni
    """
    if len(args) == 0:
        raise ValueError("Au moins un argument est requis")
    return min(args)


def maximum(*args):
    """
    Retourne le maximum des arguments.
    
    Args:
        *args: Nombres à comparer
    
    Returns:
        Le maximum des arguments
    
    Raises:
        ValueError: Si aucun argument n'est fourni
    """
    if len(args) == 0:
        raise ValueError("Au moins un argument est requis")
    return max(args)


def statistiques(*args, **kwargs):
    """
    Retourne un dictionnaire de statistiques sur les arguments.
    
    Args:
        *args: Nombres à analyser
        **kwargs: Options (precision: nombre de décimales)
    
    Returns:
        Dictionnaire avec somme, moyenne, min, max, count
    """
    if len(args) == 0:
        return {
            'somme': 0,
            'moyenne': 0,
            'minimum': None,
            'maximum': None,
            'count': 0
        }
    
    precision = kwargs.get('precision', 2)
    
    stats = {
        'somme': round(sum(args), precision),
        'moyenne': round(sum(args) / len(args), precision),
        'minimum': min(args),
        'maximum': max(args),
        'count': len(args)
    }
    
    return stats


# Exemple d'utilisation
if __name__ == "__main__":
    nombres = [10, 20, 30, 40, 50]
    
    print("Démonstration des fonctions avec paramètres variables:")
    print(f"Somme de {nombres}: {somme(*nombres)}")
    print(f"Moyenne de {nombres}: {moyenne(*nombres)}")
    print(f"Minimum de {nombres}: {minimum(*nombres)}")
    print(f"Maximum de {nombres}: {maximum(*nombres)}")
    print(f"\nStatistiques complètes:")
    stats = statistiques(*nombres, precision=3)
    for key, value in stats.items():
        print(f"  {key}: {value}")
