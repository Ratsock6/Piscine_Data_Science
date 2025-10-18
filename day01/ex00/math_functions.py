#!/usr/bin/env python3
"""
Exercise 00 - Fonctions de Base
Module contenant des fonctions mathématiques de base.
"""


def carre(n):
    """
    Retourne le carré d'un nombre.
    
    Args:
        n: Un nombre (int ou float)
    
    Returns:
        Le carré de n
    """
    return n ** 2


def cube(n):
    """
    Retourne le cube d'un nombre.
    
    Args:
        n: Un nombre (int ou float)
    
    Returns:
        Le cube de n
    """
    return n ** 3


def puissance(base, exposant):
    """
    Retourne base élevé à la puissance exposant.
    
    Args:
        base: La base (int ou float)
        exposant: L'exposant (int ou float)
    
    Returns:
        base^exposant
    """
    return base ** exposant


def factorielle(n):
    """
    Retourne la factorielle de n.
    
    Args:
        n: Un entier positif
    
    Returns:
        n! (factorielle de n)
    
    Raises:
        ValueError: Si n est négatif
    """
    if n < 0:
        raise ValueError("La factorielle n'est pas définie pour les nombres négatifs")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fibonacci(n):
    """
    Retourne le n-ième nombre de Fibonacci.
    
    Args:
        n: L'indice du nombre de Fibonacci (int >= 0)
    
    Returns:
        Le n-ième nombre de Fibonacci
    
    Raises:
        ValueError: Si n est négatif
    """
    if n < 0:
        raise ValueError("L'indice doit être positif ou zéro")
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


# Exemple d'utilisation
if __name__ == "__main__":
    print("Démonstration des fonctions mathématiques:")
    print(f"Carré de 5: {carre(5)}")
    print(f"Cube de 3: {cube(3)}")
    print(f"2 puissance 8: {puissance(2, 8)}")
    print(f"Factorielle de 5: {factorielle(5)}")
    print(f"10ème nombre de Fibonacci: {fibonacci(10)}")
