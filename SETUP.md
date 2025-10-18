# Guide de Configuration

Ce guide vous aidera à configurer votre environnement de développement pour la Piscine Data Science.

## Installation de Python

### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

### macOS
```bash
# Avec Homebrew
brew install python3
```

### Windows
Téléchargez Python depuis [python.org](https://www.python.org/downloads/)

## Configuration de l'Environnement Virtuel

Il est recommandé d'utiliser un environnement virtuel pour isoler les dépendances :

```bash
# Créer un environnement virtuel
python3 -m venv venv

# Activer l'environnement virtuel
# Sur Linux/macOS:
source venv/bin/activate

# Sur Windows:
venv\Scripts\activate
```

## Installation des Dépendances

Une fois l'environnement virtuel activé :

```bash
pip install -r requirements.txt
```

## Vérification de l'Installation

Vérifiez que tout est bien installé :

```bash
python3 -c "import numpy; print('NumPy:', numpy.__version__)"
python3 -c "import pandas; print('Pandas:', pandas.__version__)"
python3 -c "import matplotlib; print('Matplotlib:', matplotlib.__version__)"
```

## Lancement de Jupyter Notebook

Pour travailler avec Jupyter Notebook :

```bash
jupyter notebook
```

Cela ouvrira une interface web où vous pourrez créer et exécuter des notebooks.

## Structure du Projet

```
Piscine_Data_Science/
├── README.md
├── requirements.txt
├── SETUP.md
├── day00/
│   ├── README.md
│   ├── ex00/
│   ├── ex01/
│   └── ...
├── day01/
│   ├── README.md
│   ├── ex00/
│   └── ...
└── ...
```

## Conseils

1. **Toujours activer l'environnement virtuel** avant de travailler
2. **Sauvegardez régulièrement** votre travail
3. **Testez votre code** au fur et à mesure
4. **Consultez la documentation** en cas de doute
5. **N'hésitez pas à expérimenter** avec le code

## Ressources Utiles

- [Python Documentation](https://docs.python.org/3/)
- [NumPy Documentation](https://numpy.org/doc/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/)
- [Jupyter Documentation](https://jupyter.org/documentation)

## Aide

Si vous rencontrez des problèmes :
1. Vérifiez que vous avez bien activé l'environnement virtuel
2. Assurez-vous que toutes les dépendances sont installées
3. Consultez les messages d'erreur attentivement
4. Recherchez l'erreur sur Stack Overflow ou la documentation officielle

Bon courage ! 🚀
