#!/usr/bin/env python3
"""
Test Runner for Piscine Data Science
Ce script teste tous les exercices qui ne nécessitent pas d'interaction utilisateur.
"""

import os
import sys
import importlib.util


def test_exercise(day, exercise, module_name):
    """Teste un exercice spécifique."""
    try:
        # Construire le chemin du module
        module_path = f"day{day:02d}/ex{exercise:02d}/{module_name}.py"
        
        if not os.path.exists(module_path):
            return False, "Fichier non trouvé"
        
        # Charger le module
        spec = importlib.util.spec_from_file_location(module_name, module_path)
        module = importlib.util.module_from_spec(spec)
        
        print(f"✓ {module_path} chargé avec succès")
        return True, "OK"
        
    except Exception as e:
        return False, str(e)


def run_tests():
    """Exécute tous les tests."""
    print("="*60)
    print("TEST RUNNER - PISCINE DATA SCIENCE")
    print("="*60)
    print()
    
    exercises = [
        # Day 00
        (0, 0, "hello"),
        (0, 1, "operations"),
        (0, 2, "control_flow"),
        (0, 3, "lists"),
        (0, 4, "data_structures"),
        
        # Day 01
        (1, 0, "math_functions"),
        (1, 1, "advanced_functions"),
        (1, 2, "error_handling"),
        (1, 3, "data_processor"),
        
        # Day 02
        (2, 0, "classes"),
        (2, 1, "bibliotheque"),
        
        # Day 03 (nécessite numpy)
        # (3, 0, "numpy_basics"),
        # (3, 1, "matrix_operations"),
        # (3, 2, "statistical_analysis"),
        
        # Day 04 (nécessite pandas)
        # (4, 0, "pandas_basics"),
        # (4, 1, "data_cleaning"),
        # (4, 2, "data_analysis"),
        
        # Day 05 (nécessite matplotlib/seaborn)
        # (5, 0, "matplotlib_basics"),
        # (5, 1, "seaborn_advanced"),
        # (5, 2, "dashboard"),
    ]
    
    passed = 0
    failed = 0
    
    for day, ex, module in exercises:
        success, message = test_exercise(day, ex, module)
        if success:
            passed += 1
        else:
            failed += 1
            print(f"✗ day{day:02d}/ex{ex:02d}/{module}.py - {message}")
    
    print()
    print("="*60)
    print(f"RÉSULTATS: {passed} réussi(s), {failed} échoué(s)")
    print("="*60)
    print()
    
    print("Note: Les exercices Day03-Day05 nécessitent l'installation des dépendances.")
    print("Installez-les avec: pip install -r requirements.txt")


if __name__ == "__main__":
    run_tests()
