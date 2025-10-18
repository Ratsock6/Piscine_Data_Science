#!/usr/bin/env python3
"""
Exercise 04 - Dictionnaires et Ensembles
Ce programme démontre l'utilisation de dictionnaires et d'ensembles.
"""

# Créer un dictionnaire représentant un étudiant
etudiant = {
    "nom": "Dupont",
    "prenom": "Jean",
    "age": 22,
    "notes": [15, 18, 12, 16]
}

print("Étudiant initial:")
print(etudiant)

# Ajouter une entrée
etudiant["email"] = "jean.dupont@example.com"
print("\nAprès ajout de l'email:")
print(etudiant)

# Modifier une entrée
etudiant["age"] = 23
print("\nAprès modification de l'âge:")
print(etudiant)

# Ajouter une note
etudiant["notes"].append(17)
print("\nAprès ajout d'une note:")
print(etudiant)

# Calculer la moyenne des notes
moyenne_notes = sum(etudiant["notes"]) / len(etudiant["notes"])
print(f"\nMoyenne des notes: {moyenne_notes:.2f}")

# Supprimer une entrée
del etudiant["email"]
print("\nAprès suppression de l'email:")
print(etudiant)

# Démonstration des ensembles
print("\n" + "="*50)
print("ENSEMBLES")
print("="*50)

# Créer des ensembles
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"\nEnsemble 1: {set1}")
print(f"Ensemble 2: {set2}")

# Union
union = set1 | set2
print(f"\nUnion (set1 | set2): {union}")

# Intersection
intersection = set1 & set2
print(f"Intersection (set1 & set2): {intersection}")

# Différence
difference = set1 - set2
print(f"Différence (set1 - set2): {difference}")

# Différence symétrique
diff_sym = set1 ^ set2
print(f"Différence symétrique (set1 ^ set2): {diff_sym}")

# Opérations sur les ensembles
set1.add(9)
print(f"\nAprès ajout de 9 à set1: {set1}")

set1.remove(1)
print(f"Après suppression de 1 de set1: {set1}")
