#!/usr/bin/env python3
"""
Exercise 03 - Manipulation de Listes
Ce programme démontre la manipulation de listes en Python.
"""

# Créer une liste de nombres
nombres = [5, 2, 8, 1, 9, 3, 7]
print("Liste initiale:", nombres)

# Ajouter des éléments à la liste
nombres.append(10)
print("Après ajout de 10:", nombres)

nombres.extend([4, 6])
print("Après extension avec [4, 6]:", nombres)

# Supprimer des éléments de la liste
nombres.remove(1)  # Supprime la première occurrence de 1
print("Après suppression de 1:", nombres)

dernier = nombres.pop()  # Supprime et retourne le dernier élément
print(f"Dernier élément supprimé: {dernier}")
print("Après pop():", nombres)

# Trier la liste
nombres_tries = sorted(nombres)  # Crée une nouvelle liste triée
print("Liste triée (nouvelle liste):", nombres_tries)

nombres.sort()  # Trie la liste en place
print("Liste triée (en place):", nombres)

# Calculer la somme et la moyenne des éléments
total = sum(nombres)
moyenne = total / len(nombres) if len(nombres) > 0 else 0

print(f"\nStatistiques:")
print(f"Somme: {total}")
print(f"Moyenne: {moyenne:.2f}")
print(f"Nombre d'éléments: {len(nombres)}")
print(f"Minimum: {min(nombres)}")
print(f"Maximum: {max(nombres)}")
