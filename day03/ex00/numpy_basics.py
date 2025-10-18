#!/usr/bin/env python3
"""
Exercise 00 - Introduction à NumPy
Démonstration des concepts de base de NumPy.
"""

import numpy as np


def demonstration_arrays():
    """Démonstration de la création d'arrays."""
    print("=== Création d'Arrays ===\n")
    
    # Créer un array à partir d'une liste
    arr1 = np.array([1, 2, 3, 4, 5])
    print(f"Array depuis une liste: {arr1}")
    print(f"Type: {type(arr1)}, dtype: {arr1.dtype}\n")
    
    # Array 2D
    arr2d = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"Array 2D:\n{arr2d}")
    print(f"Shape: {arr2d.shape}, Size: {arr2d.size}\n")
    
    # Arrays spéciaux
    zeros = np.zeros((3, 3))
    ones = np.ones((2, 4))
    identity = np.eye(3)
    
    print(f"Zeros (3x3):\n{zeros}\n")
    print(f"Ones (2x4):\n{ones}\n")
    print(f"Identité (3x3):\n{identity}\n")
    
    # Séquences
    arange = np.arange(0, 10, 2)
    linspace = np.linspace(0, 1, 5)
    
    print(f"Arange (0 à 10, pas de 2): {arange}")
    print(f"Linspace (5 valeurs entre 0 et 1): {linspace}\n")


def operations_vectorielles():
    """Démonstration des opérations vectorielles."""
    print("=== Opérations Vectorielles ===\n")
    
    a = np.array([1, 2, 3, 4, 5])
    b = np.array([5, 4, 3, 2, 1])
    
    print(f"a = {a}")
    print(f"b = {b}\n")
    
    print(f"a + b = {a + b}")
    print(f"a - b = {a - b}")
    print(f"a * b = {a * b}")
    print(f"a / b = {a / b}")
    print(f"a ** 2 = {a ** 2}\n")


def indexation_slicing():
    """Démonstration de l'indexation et du slicing."""
    print("=== Indexation et Slicing ===\n")
    
    arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(f"Array: {arr}\n")
    
    print(f"arr[0] = {arr[0]}")
    print(f"arr[-1] = {arr[-1]}")
    print(f"arr[2:5] = {arr[2:5]}")
    print(f"arr[::2] = {arr[::2]}")
    print(f"arr[::-1] = {arr[::-1]}\n")
    
    # 2D indexation
    arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f"Array 2D:\n{arr2d}\n")
    print(f"arr2d[1, 2] = {arr2d[1, 2]}")
    print(f"arr2d[:, 1] = {arr2d[:, 1]}")
    print(f"arr2d[1, :] = {arr2d[1, :]}\n")


def fonctions_mathematiques():
    """Démonstration des fonctions mathématiques."""
    print("=== Fonctions Mathématiques ===\n")
    
    arr = np.array([1, 2, 3, 4, 5])
    print(f"Array: {arr}\n")
    
    print(f"Somme: {np.sum(arr)}")
    print(f"Moyenne: {np.mean(arr)}")
    print(f"Médiane: {np.median(arr)}")
    print(f"Écart-type: {np.std(arr)}")
    print(f"Min: {np.min(arr)}, Max: {np.max(arr)}")
    print(f"Racine carrée: {np.sqrt(arr)}")
    print(f"Exponentielle: {np.exp(arr)}\n")


def broadcasting():
    """Démonstration du broadcasting."""
    print("=== Broadcasting ===\n")
    
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    scalar = 10
    
    print(f"Array:\n{arr}\n")
    print(f"Array + {scalar}:\n{arr + scalar}\n")
    
    vec = np.array([1, 2, 3])
    print(f"Vecteur: {vec}")
    print(f"Array + vecteur:\n{arr + vec}\n")


if __name__ == "__main__":
    demonstration_arrays()
    operations_vectorielles()
    indexation_slicing()
    fonctions_mathematiques()
    broadcasting()
