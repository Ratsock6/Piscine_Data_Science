#!/usr/bin/env python3
"""
Exercise 01 - Opérations Arithmétiques
Ce programme effectue des opérations arithmétiques de base.
"""

# Demander deux nombres à l'utilisateur
num1 = float(input("Entrez le premier nombre: "))
num2 = float(input("Entrez le deuxième nombre: "))

# Effectuer les opérations
somme = num1 + num2
difference = num1 - num2
produit = num1 * num2
quotient = num1 / num2 if num2 != 0 else "Division par zéro impossible"
reste = num1 % num2 if num2 != 0 else "Division par zéro impossible"

# Afficher les résultats
print(f"\nRésultats:")
print(f"{num1} + {num2} = {somme}")
print(f"{num1} - {num2} = {difference}")
print(f"{num1} * {num2} = {produit}")
print(f"{num1} / {num2} = {quotient}")
print(f"{num1} % {num2} = {reste}")
