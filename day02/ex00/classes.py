#!/usr/bin/env python3
"""
Exercise 00 - Classes de Base
Démonstration des concepts de base de la POO avec héritage.
"""


class Personne:
    """
    Classe de base représentant une personne.
    """
    
    def __init__(self, nom, prenom, age):
        """
        Initialise une personne.
        
        Args:
            nom: Nom de famille
            prenom: Prénom
            age: Âge de la personne
        """
        self.nom = nom
        self.prenom = prenom
        self.age = age
    
    def se_presenter(self):
        """Retourne une présentation de la personne."""
        return f"Bonjour, je m'appelle {self.prenom} {self.nom} et j'ai {self.age} ans."
    
    def vieillir(self):
        """Incrémente l'âge de la personne."""
        self.age += 1
        print(f"{self.prenom} a maintenant {self.age} ans.")
    
    def __str__(self):
        """Représentation en chaîne de la personne."""
        return f"{self.prenom} {self.nom}, {self.age} ans"
    
    def __repr__(self):
        """Représentation officielle de la personne."""
        return f"Personne('{self.nom}', '{self.prenom}', {self.age})"


class Etudiant(Personne):
    """
    Classe représentant un étudiant, hérite de Personne.
    """
    
    def __init__(self, nom, prenom, age, niveau, notes=None):
        """
        Initialise un étudiant.
        
        Args:
            nom: Nom de famille
            prenom: Prénom
            age: Âge
            niveau: Niveau d'études (ex: "L1", "M2")
            notes: Liste de notes (optionnel)
        """
        super().__init__(nom, prenom, age)
        self.niveau = niveau
        self.notes = notes if notes is not None else []
    
    def ajouter_note(self, note):
        """
        Ajoute une note à la liste des notes.
        
        Args:
            note: Note à ajouter (entre 0 et 20)
        """
        if 0 <= note <= 20:
            self.notes.append(note)
        else:
            raise ValueError("La note doit être entre 0 et 20")
    
    def moyenne(self):
        """
        Calcule la moyenne des notes.
        
        Returns:
            La moyenne des notes, ou None si pas de notes
        """
        if not self.notes:
            return None
        return sum(self.notes) / len(self.notes)
    
    def se_presenter(self):
        """Retourne une présentation de l'étudiant."""
        base = super().se_presenter()
        moyenne = self.moyenne()
        if moyenne is not None:
            return f"{base} Je suis en {self.niveau} avec une moyenne de {moyenne:.2f}/20."
        return f"{base} Je suis en {self.niveau}."
    
    def __str__(self):
        """Représentation en chaîne de l'étudiant."""
        return f"{super().__str__()}, {self.niveau}"


class Professeur(Personne):
    """
    Classe représentant un professeur, hérite de Personne.
    """
    
    def __init__(self, nom, prenom, age, matiere, salaire):
        """
        Initialise un professeur.
        
        Args:
            nom: Nom de famille
            prenom: Prénom
            age: Âge
            matiere: Matière enseignée
            salaire: Salaire mensuel
        """
        super().__init__(nom, prenom, age)
        self.matiere = matiere
        self._salaire = salaire  # Attribut protégé
    
    @property
    def salaire(self):
        """Getter pour le salaire."""
        return self._salaire
    
    @salaire.setter
    def salaire(self, nouveau_salaire):
        """
        Setter pour le salaire.
        
        Args:
            nouveau_salaire: Nouveau salaire (doit être positif)
        """
        if nouveau_salaire > 0:
            self._salaire = nouveau_salaire
        else:
            raise ValueError("Le salaire doit être positif")
    
    def se_presenter(self):
        """Retourne une présentation du professeur."""
        base = super().se_presenter()
        return f"{base} J'enseigne {self.matiere}."
    
    def augmentation(self, pourcentage):
        """
        Applique une augmentation de salaire.
        
        Args:
            pourcentage: Pourcentage d'augmentation
        """
        ancien_salaire = self._salaire
        self._salaire *= (1 + pourcentage / 100)
        print(f"Salaire augmenté de {pourcentage}%: {ancien_salaire:.2f}€ → {self._salaire:.2f}€")
    
    def __str__(self):
        """Représentation en chaîne du professeur."""
        return f"{super().__str__()}, Professeur de {self.matiere}"


# Exemple d'utilisation
if __name__ == "__main__":
    print("=== Démonstration de la POO ===\n")
    
    # Créer des personnes
    personne = Personne("Dupont", "Jean", 30)
    print(personne.se_presenter())
    print()
    
    # Créer un étudiant
    etudiant = Etudiant("Martin", "Sophie", 20, "M1")
    etudiant.ajouter_note(15)
    etudiant.ajouter_note(18)
    etudiant.ajouter_note(16)
    print(etudiant.se_presenter())
    print(f"Notes: {etudiant.notes}")
    print()
    
    # Créer un professeur
    prof = Professeur("Durand", "Marie", 45, "Mathématiques", 3000)
    print(prof.se_presenter())
    prof.augmentation(10)
    print()
    
    # Démonstration du polymorphisme
    print("=== Polymorphisme ===")
    personnes = [personne, etudiant, prof]
    for p in personnes:
        print(f"- {p.se_presenter()}")
