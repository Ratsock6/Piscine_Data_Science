#!/usr/bin/env python3
"""
Exercise 02 - Gestion des Exceptions
Programme démontrant la gestion robuste des erreurs.
"""


class DivisionParZeroError(Exception):
    """Exception personnalisée pour la division par zéro."""
    pass


class NombreNegatifError(Exception):
    """Exception personnalisée pour les nombres négatifs non autorisés."""
    pass


def division_securisee(dividende, diviseur):
    """
    Effectue une division avec gestion des erreurs.
    
    Args:
        dividende: Le nombre à diviser
        diviseur: Le nombre par lequel diviser
    
    Returns:
        Le résultat de la division
    
    Raises:
        DivisionParZeroError: Si le diviseur est zéro
        TypeError: Si les arguments ne sont pas des nombres
    """
    try:
        if diviseur == 0:
            raise DivisionParZeroError("Impossible de diviser par zéro!")
        return dividende / diviseur
    except TypeError:
        raise TypeError("Les arguments doivent être des nombres")


def racine_carree(nombre):
    """
    Calcule la racine carrée d'un nombre.
    
    Args:
        nombre: Le nombre dont on veut la racine carrée
    
    Returns:
        La racine carrée du nombre
    
    Raises:
        NombreNegatifError: Si le nombre est négatif
    """
    if nombre < 0:
        raise NombreNegatifError("Impossible de calculer la racine carrée d'un nombre négatif")
    return nombre ** 0.5


def main():
    """Fonction principale avec gestion interactive des erreurs."""
    print("=== Programme de Division Sécurisée ===\n")
    
    while True:
        try:
            # Demander les nombres à l'utilisateur
            dividende = float(input("Entrez le dividende (ou 'q' pour quitter): "))
            diviseur = float(input("Entrez le diviseur: "))
            
            # Effectuer la division
            resultat = division_securisee(dividende, diviseur)
            print(f"\nRésultat: {dividende} / {diviseur} = {resultat:.2f}")
            
            # Calculer la racine carrée du résultat si positif
            if resultat >= 0:
                racine = racine_carree(resultat)
                print(f"Racine carrée du résultat: {racine:.2f}")
            else:
                print("Le résultat est négatif, impossible de calculer la racine carrée")
            
            print()
            
        except ValueError as e:
            # Vérifier si l'utilisateur veut quitter
            reponse = input("Entrez le dividende (ou 'q' pour quitter): ")
            if reponse.lower() == 'q':
                print("Au revoir!")
                break
            print(f"Erreur: Veuillez entrer des nombres valides\n")
            
        except DivisionParZeroError as e:
            print(f"Erreur: {e}\n")
            
        except NombreNegatifError as e:
            print(f"Erreur: {e}\n")
            
        except KeyboardInterrupt:
            print("\n\nProgramme interrompu par l'utilisateur. Au revoir!")
            break
            
        except Exception as e:
            print(f"Erreur inattendue: {e}\n")


if __name__ == "__main__":
    # Démonstration sans interaction
    print("Démonstration de la gestion des exceptions:\n")
    
    # Test 1: Division normale
    try:
        print(f"10 / 2 = {division_securisee(10, 2)}")
    except Exception as e:
        print(f"Erreur: {e}")
    
    # Test 2: Division par zéro
    try:
        print(f"10 / 0 = {division_securisee(10, 0)}")
    except DivisionParZeroError as e:
        print(f"Erreur attendue: {e}")
    
    # Test 3: Racine carrée d'un nombre négatif
    try:
        print(f"Racine de -4 = {racine_carree(-4)}")
    except NombreNegatifError as e:
        print(f"Erreur attendue: {e}")
    
    # Test 4: Type invalide
    try:
        print(f"'10' / 2 = {division_securisee('10', 2)}")
    except TypeError as e:
        print(f"Erreur attendue: {e}")
    
    print("\n" + "="*50)
    print("Pour tester la version interactive, décommentez la ligne suivante:")
    print("# main()")
