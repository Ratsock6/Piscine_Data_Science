# Day 01 - Fonctions et Modules

Bienvenue au deuxième jour de la Piscine Data Science ! Aujourd'hui, nous allons apprendre à structurer notre code avec des fonctions et des modules.

## 📚 Objectifs du jour

- Créer et utiliser des fonctions
- Comprendre les arguments et paramètres
- Maîtriser la portée des variables
- Organiser le code en modules
- Gérer les erreurs et exceptions

## 📝 Exercices

### Exercice 00 - Fonctions de Base
**Dossier :** `ex00/`

Créer un module avec des fonctions mathématiques.

**Fichier à créer :** `math_functions.py`

Implémenter les fonctions suivantes :
- `carre(n)` : retourne le carré d'un nombre
- `cube(n)` : retourne le cube d'un nombre
- `puissance(base, exposant)` : retourne base^exposant
- `factorielle(n)` : retourne n!
- `fibonacci(n)` : retourne le n-ième nombre de Fibonacci

### Exercice 01 - Fonctions avec Paramètres Variables
**Dossier :** `ex01/`

Créer des fonctions qui acceptent un nombre variable d'arguments.

**Fichier à créer :** `advanced_functions.py`

Implémenter :
- `somme(*args)` : retourne la somme de tous les arguments
- `moyenne(*args)` : retourne la moyenne des arguments
- `minimum(*args)` : retourne le minimum
- `maximum(*args)` : retourne le maximum
- `statistiques(*args, **kwargs)` : retourne un dictionnaire de statistiques

### Exercice 02 - Gestion des Exceptions
**Dossier :** `ex02/`

Créer un programme robuste qui gère les erreurs.

**Fichier à créer :** `error_handling.py`

Le programme doit :
- Demander à l'utilisateur d'entrer deux nombres
- Effectuer la division
- Gérer les exceptions (ValueError, ZeroDivisionError)
- Créer des exceptions personnalisées

### Exercice 03 - Module de Traitement de Données
**Dossier :** `ex03/`

Créer un module complet pour traiter des données.

**Fichiers à créer :** 
- `data_processor.py` : module principal
- `test_data_processor.py` : tests du module

Le module doit contenir :
- `lire_nombres(fichier)` : lit des nombres depuis un fichier
- `filtrer_pairs(liste)` : retourne uniquement les nombres pairs
- `filtrer_impairs(liste)` : retourne uniquement les nombres impairs
- `appliquer_fonction(liste, fonction)` : applique une fonction à chaque élément

## 🎯 Conseils

- Utilisez des docstrings pour documenter vos fonctions
- Testez vos fonctions avec différents types d'entrées
- Gérez les cas limites (listes vides, nombres négatifs, etc.)
- Utilisez des noms de fonctions descriptifs

## 📖 Ressources

- [Python Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Python Modules](https://docs.python.org/3/tutorial/modules.html)
- [Python Exceptions](https://docs.python.org/3/tutorial/errors.html)

Bon courage ! 🚀
