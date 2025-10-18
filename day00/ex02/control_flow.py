#!/usr/bin/env python3
"""
Exercise 02 - Structures de Contrôle
Ce programme démontre l'utilisation des structures de contrôle.
"""

# Demander un nombre à l'utilisateur
nombre = int(input("Entrez un nombre: "))

# Déterminer si le nombre est positif, négatif ou zéro
if nombre > 0:
    print(f"{nombre} est positif")
elif nombre < 0:
    print(f"{nombre} est négatif")
else:
    print("Le nombre est zéro")

# Déterminer si le nombre est pair ou impair
if nombre % 2 == 0:
    print(f"{nombre} est pair")
else:
    print(f"{nombre} est impair")

# Afficher tous les nombres de 1 à ce nombre
if nombre > 0:
    print(f"\nNombres de 1 à {nombre}:")
    for i in range(1, nombre + 1):
        print(i, end=" ")
    print()  # Nouvelle ligne
elif nombre < 0:
    print(f"\nNombres de {nombre} à -1:")
    for i in range(nombre, 0):
        print(i, end=" ")
    print()  # Nouvelle ligne
