#!/usr/bin/env python3
"""
Exercise 01 - Opérations Matricielles
Démonstration des opérations d'algèbre linéaire avec NumPy.
"""

import numpy as np


def operations_matrices():
    """Démonstration des opérations matricielles de base."""
    print("=== Opérations Matricielles ===\n")
    
    # Créer des matrices
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    
    print("Matrice A:")
    print(A)
    print("\nMatrice B:")
    print(B)
    print()
    
    # Addition et soustraction
    print("A + B:")
    print(A + B)
    print("\nA - B:")
    print(A - B)
    print()
    
    # Multiplication matricielle
    print("Produit matriciel (A @ B):")
    print(A @ B)
    print("\nProduit élément par élément (A * B):")
    print(A * B)
    print()
    
    # Transposition
    print("Transposée de A:")
    print(A.T)
    print()


def determinant_inverse():
    """Calcul du déterminant et de l'inverse."""
    print("=== Déterminant et Inverse ===\n")
    
    A = np.array([[4, 7], [2, 6]])
    print("Matrice A:")
    print(A)
    print()
    
    # Déterminant
    det = np.linalg.det(A)
    print(f"Déterminant de A: {det}")
    print()
    
    # Inverse
    if det != 0:
        inv_A = np.linalg.inv(A)
        print("Inverse de A:")
        print(inv_A)
        print()
        
        # Vérification: A @ inv(A) = I
        print("Vérification A @ inv(A):")
        print(A @ inv_A)
        print()


def systeme_equations():
    """Résolution de système d'équations linéaires."""
    print("=== Système d'Équations Linéaires ===\n")
    
    # Système: 2x + 3y = 8
    #          3x + 2y = 7
    A = np.array([[2, 3], [3, 2]])
    b = np.array([8, 7])
    
    print("Système d'équations:")
    print("2x + 3y = 8")
    print("3x + 2y = 7")
    print()
    
    # Solution
    x = np.linalg.solve(A, b)
    print(f"Solution: x = {x[0]}, y = {x[1]}")
    print()
    
    # Vérification
    print("Vérification:")
    print(f"2*{x[0]} + 3*{x[1]} = {2*x[0] + 3*x[1]}")
    print(f"3*{x[0]} + 2*{x[1]} = {3*x[0] + 2*x[1]}")
    print()


def valeurs_propres():
    """Calcul des valeurs et vecteurs propres."""
    print("=== Valeurs et Vecteurs Propres ===\n")
    
    A = np.array([[4, -2], [1, 1]])
    print("Matrice A:")
    print(A)
    print()
    
    # Valeurs et vecteurs propres
    eigenvalues, eigenvectors = np.linalg.eig(A)
    
    print("Valeurs propres:")
    print(eigenvalues)
    print("\nVecteurs propres:")
    print(eigenvectors)
    print()


if __name__ == "__main__":
    operations_matrices()
    determinant_inverse()
    systeme_equations()
    valeurs_propres()
