#!/usr/bin/env python3
"""
Exercise 01 - Système de Gestion de Bibliothèque
Implémentation d'un système de bibliothèque avec POO.
"""

from datetime import datetime, timedelta


class Livre:
    """Classe représentant un livre."""
    
    def __init__(self, titre, auteur, isbn):
        """
        Initialise un livre.
        
        Args:
            titre: Titre du livre
            auteur: Auteur du livre
            isbn: Numéro ISBN
        """
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn
        self.disponible = True
        self.date_emprunt = None
    
    def emprunter(self):
        """Marque le livre comme emprunté."""
        if self.disponible:
            self.disponible = False
            self.date_emprunt = datetime.now()
            return True
        return False
    
    def retourner(self):
        """Marque le livre comme retourné."""
        self.disponible = True
        self.date_emprunt = None
    
    def __str__(self):
        """Représentation en chaîne du livre."""
        status = "Disponible" if self.disponible else "Emprunté"
        return f"'{self.titre}' par {self.auteur} ({self.isbn}) - {status}"


class Membre:
    """Classe représentant un membre de la bibliothèque."""
    
    def __init__(self, nom, numero_membre):
        """
        Initialise un membre.
        
        Args:
            nom: Nom du membre
            numero_membre: Numéro unique du membre
        """
        self.nom = nom
        self.numero_membre = numero_membre
        self.livres_empruntes = []
    
    def emprunter_livre(self, livre):
        """
        Emprunte un livre.
        
        Args:
            livre: Instance de Livre à emprunter
        
        Returns:
            True si succès, False sinon
        """
        if livre.emprunter():
            self.livres_empruntes.append(livre)
            print(f"{self.nom} a emprunté '{livre.titre}'")
            return True
        print(f"'{livre.titre}' n'est pas disponible")
        return False
    
    def retourner_livre(self, livre):
        """
        Retourne un livre.
        
        Args:
            livre: Instance de Livre à retourner
        """
        if livre in self.livres_empruntes:
            livre.retourner()
            self.livres_empruntes.remove(livre)
            print(f"{self.nom} a retourné '{livre.titre}'")
        else:
            print(f"{self.nom} n'a pas emprunté '{livre.titre}'")
    
    def afficher_emprunts(self):
        """Affiche les livres actuellement empruntés."""
        if not self.livres_empruntes:
            print(f"{self.nom} n'a aucun livre emprunté")
        else:
            print(f"{self.nom} a emprunté:")
            for livre in self.livres_empruntes:
                print(f"  - {livre.titre}")
    
    def __str__(self):
        """Représentation en chaîne du membre."""
        return f"Membre {self.numero_membre}: {self.nom} ({len(self.livres_empruntes)} livre(s) emprunté(s))"


class Bibliotheque:
    """Classe représentant une bibliothèque."""
    
    def __init__(self, nom):
        """
        Initialise une bibliothèque.
        
        Args:
            nom: Nom de la bibliothèque
        """
        self.nom = nom
        self.catalogue = []
        self.membres = []
    
    def ajouter_livre(self, livre):
        """Ajoute un livre au catalogue."""
        self.catalogue.append(livre)
        print(f"Livre ajouté: {livre.titre}")
    
    def ajouter_membre(self, membre):
        """Ajoute un membre à la bibliothèque."""
        self.membres.append(membre)
        print(f"Membre inscrit: {membre.nom}")
    
    def rechercher_livre(self, titre):
        """
        Recherche un livre par titre.
        
        Args:
            titre: Titre à rechercher
        
        Returns:
            Liste des livres trouvés
        """
        return [livre for livre in self.catalogue if titre.lower() in livre.titre.lower()]
    
    def livres_disponibles(self):
        """Retourne la liste des livres disponibles."""
        return [livre for livre in self.catalogue if livre.disponible]
    
    def afficher_catalogue(self):
        """Affiche le catalogue complet."""
        print(f"\n=== Catalogue de {self.nom} ===")
        if not self.catalogue:
            print("Aucun livre dans le catalogue")
        else:
            for livre in self.catalogue:
                print(f"  {livre}")
    
    def afficher_statistiques(self):
        """Affiche les statistiques de la bibliothèque."""
        total = len(self.catalogue)
        disponibles = len(self.livres_disponibles())
        empruntes = total - disponibles
        
        print(f"\n=== Statistiques de {self.nom} ===")
        print(f"Total de livres: {total}")
        print(f"Livres disponibles: {disponibles}")
        print(f"Livres empruntés: {empruntes}")
        print(f"Nombre de membres: {len(self.membres)}")


# Exemple d'utilisation
if __name__ == "__main__":
    # Créer une bibliothèque
    biblio = Bibliotheque("Bibliothèque Municipale")
    
    # Ajouter des livres
    livre1 = Livre("Python pour les Data Scientists", "Jake VanderPlas", "978-1491912058")
    livre2 = Livre("Data Science Handbook", "Field Cady", "978-1119092940")
    livre3 = Livre("Python Data Science", "Wes McKinney", "978-1491957660")
    
    biblio.ajouter_livre(livre1)
    biblio.ajouter_livre(livre2)
    biblio.ajouter_livre(livre3)
    
    # Ajouter des membres
    membre1 = Membre("Alice Dupont", "M001")
    membre2 = Membre("Bob Martin", "M002")
    
    biblio.ajouter_membre(membre1)
    biblio.ajouter_membre(membre2)
    
    print()
    biblio.afficher_catalogue()
    
    # Emprunts
    print("\n=== Emprunts ===")
    membre1.emprunter_livre(livre1)
    membre1.emprunter_livre(livre2)
    membre2.emprunter_livre(livre1)  # Déjà emprunté
    membre2.emprunter_livre(livre3)
    
    print()
    biblio.afficher_catalogue()
    
    # Afficher les emprunts des membres
    print("\n=== Emprunts des membres ===")
    membre1.afficher_emprunts()
    membre2.afficher_emprunts()
    
    # Retours
    print("\n=== Retours ===")
    membre1.retourner_livre(livre1)
    
    print()
    biblio.afficher_catalogue()
    
    # Statistiques
    biblio.afficher_statistiques()
