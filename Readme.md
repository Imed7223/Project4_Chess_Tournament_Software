# Programme de gestion de tournois d'échecs
## Introduction

Ce programme Python permet de gérer les tournois d'échecs pour un club de manière autonome et hors ligne.
Il inclut des fonctionnalités de gestion des joueurs, des tournois, des tours, et des rapports, 
tout en respectant les standards de la programmation orientée objet et du design pattern MVC (Modèle-Vue-Contrôleur).
## Table des matières

    1-Prérequis
        Installation des dépendances
        Exécution du script
    2-Fonctionnalités
        Phases du programme
    3-Structure du projet
    4-Fichiers générés
    5-Génération du rapport flake8-html

## Prérequis
### Installation des dépendances

Ce projet nécessite plusieurs bibliothèques Python pour fonctionner correctement. 
Vous pouvez installer toutes les dépendances à l'aide du fichier requirements.txt.
Étapes pour installer les dépendances :

    1-Installer Python : Assurez-vous d'avoir Python installé sur votre machine.
 
    2-Créer un environnement virtuel (recommandé) :  
`python -m venv venv`
 
    3-Activer l'environnement virtuel :  
    Sous Windows :  
`venv\Scripts\activate`  

    Sous macOS/Linux :  
`source venv/bin/activate`
    
    4-Installer les dépendances :  
`python -m pip install -r requirements.txt`

### Exécution du script

Une fois les dépendances installées, vous pouvez exécuter le script principal pour le Logiciel de tournoi d’échecs.
Pour exécuter le script :

    1-Ouvrez un terminal ou une invite de commandes.

    2-Assurez-vous que l'environnement virtuel est activé (si utilisé).

    3-Exécutez le script en utilisant la commande suivante :

`python main.py`

## Fonctionnalités

Le script est divisé en plusieurs phases pour lancer le Logiciel de tournoi d’échecs et l'organiser. 
Le script s'exécute dans la console et sauvegarde toutes les données dans des fichiers JSON, 
garantissant la persistance entre les sessions.

### Phases du programme

    1-Ajouter un nouveau tournoi : Permet de créer un nouveau tournoi en saisissant des informations comme le nom, le lieu, les dates, et les joueurs inscrits.

    2-Sélectionner des tournois : Offre la possibilité de sélectionner des tournois spécifiques pour les consulter ou effectuer des actions supplémentaires.

    3-Sélectionner des joueurs : Permet de gérer les joueurs participants au tournoi.

    4-Commencer et jouer 4 tours : Lance automatiquement un tournoi avec 4 tours, en générant les paires de joueurs et en enregistrant les résultats.

    5-Lister les joueurs candidats par ordre alphabétique : Affiche une liste triée alphabétiquement de tous les joueurs inscrits.

    6-Afficher les tournois disponibles : Montre tous les tournois enregistrés dans le programme.

    7-Détails d'un tournoi sélectionné : Fournit des informations détaillées sur un tournoi spécifique, comme les participants et les résultats.

    8-Lister les joueurs d'un tournoi par ordre alphabétique : Affiche les participants d'un tournoi donné, triés par ordre alphabétique.

    9-Afficher les détails de tous les tours et matchs avec le classement des joueurs : Donne une vue complète des résultats des tours, des matchs joués, 
	et du classement des joueurs pour tous les tournois.

    10-Afficher et sauvegarder le classement des joueurs : Génère et enregistre un rapport sur le classement actuel des joueurs.

    11-Quitter : Termine l'exécution du programme.

## Structure du projet

Voici la structure des fichiers et dossiers du projet :
```

/mon-projet-de-python/
│
├── main.py                     # Point d'entrée du programme
├── requirements.txt            # Liste des dépendances
├── README.md                   # Documentation du projet
├── .gitignore                  # Exclusion des fichiers pycache, .venv, .idea
│
├── controllers/                # Dossier contenant les contrôleurs
│   └── controller.py           # Logique de contrôle du programme
│
├── views/                      # Dossier contenant les 
    ├── json_manager.py             # Gestion des fichiers JSON
│   └── menu.py                 # Interface utilisateur en console  
│
├── models/                     # Dossier contenant les modèles
│   ├── model_player.py         # Modèle pour les joueurs
│   ├── model_tournament.py     # Modèle pour les tournois
│   ├── model_round.py          # Modèle pour les tours
│   └── model_match.py          # Modèle pour les matchs
│
└── flake8_report/              # Rapports de formatage et de nettoyage du code
```
## Fichiers générés

    Fichiers JSON : Les données des tournois, des joueurs, des tours et des matchs sont sauvegardées dans des fichiers 
                    JSON pour assurer la persistance des données entre les sessions.
    Rapports : Les rapports de classement et les détails des tournois sont générés et sauvegardés dans des fichiers JSON.

## Génération du rapport flake8-html
Pour vérifier la qualité du code et générer un rapport flake8-html, suivez les étapes suivantes :

   1-Assurez-vous que flake8 et flake8-html sont installés. Si ce n'est pas le cas, installez-les via pip :
   
`python -m pip install flake8 flake8-html`
   
   2-Exécutez la commande suivante pour générer le rapport :

`flake8 --format=html --htmldir=flake8_report`
   
   3-Le rapport sera généré dans le dossier flake8_report. Ouvrez le fichier index.html pour visualiser les résultats.
