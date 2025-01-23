# Programme de gestion de tournois d'échecs

## Introduction

Ce programme Python permet de gérer les tournois d'échecs pour un club de manière autonome et hors ligne.
 Il inclut des fonctionnalités de gestion des joueurs, des tournois, des tours, et des rapports,
 tout en respectant les standards de la programmation orientée objet et du design pattern MVC.

---

## Prérequis

1/## Installation des dépendances

Ce projet nécessite plusieurs bibliothèques Python pour fonctionner correctement.
 Vous pouvez installer toutes les dépendances à l'aide du fichier requirements.txt.

Étapes pour installer les dépendances :
Assurez-vous d'avoir Python installé sur votre machine.
Créez un environnement virtuel (recommandé) :
python -m venv venv
3.Activez l'environnement virtuel :

Sous Windows :

venv\Scripts\activate

4.Installez les dépendances en utilisant le fichier requirements.txt:
pip install -r requirements.txt

2/## Exécution du script

Une fois les dépendances installées, vous pouvez exécuter le script principal pour le Logiciel de tournoi d’échecs.

### Pour exécuter le script :
1. Ouvrez un terminal ou une invite de commandes.
2. Assurez-vous que l'environnement virtuel est activé (si utilisé).
3. Exécutez le script en utilisant la commande suivante :
  ```bash
  python main.py

3/###  **Description du fonctionnement du script**
Le script est divisé en plusieurs phases pour lancer le Logiciel de tournoi d’échecs et l'organiser.
Le script s'exécute dans la console et sauvegarde toutes les données dans des fichiers JSON, garantissant la persistance entre les sessions.


### Phase 1 : Ajouter un nouveau tournoi : 
Permet de créer un nouveau tournoi en saisissant des informations comme le nom, le lieu, les dates, et les joueurs inscrits.

### Phase 2 : Sélectionner des tournois : 
Offre la possibilité de sélectionner des tournois spécifiques pour les consulter ou effectuer des actions supplémentaires.

### Phase 3 : Sélectionner des joueurs : Permet de gérer les joueurs participants au tournoi.

### Phase 4 : Commencer et jouer 4 tours : 
Lance automatiquement un tournoi avec 4 tours, en générant les paires de joueurs et en enregistrant les résultats.

### Phase 5 : Lister les joueurs candidats par ordre alphabétique : 
Affiche une liste triée alphabétiquement de tous les joueurs inscrits.

### Phase 6 : Afficher les tournois disponibles : Montre tous les tournois enregistrés dans le programme.

### Phase 7 : Détails d'un tournoi sélectionné : Fournit des informations détaillées sur un tournoi spécifique, 
comme les participants et les résultats.

### Phase 8 : Lister les joueurs d'un tournoi par ordre alphabétique : Affiche les participants d'un tournoi donné,
 triés par ordre alphabétique.

### Phase 9 : Afficher les détails de tous les tours et matchs avec le classement des joueurs : Donne une vue complète des résultats des tours, 
des matchs joués, et du classement des joueurs pour tous les tournois.

### Phase 10 : Afficher et sauvegarder le classement des joueurs : Génère et enregistre un rapport sur le classement actuel des joueurs.

### Phase 11 : Quitter : Termine l'exécution du programme.


### Structure des fichiers générés :
- Les fichiers CSV sont stockés dans le répertoire racine du projet.
- Les images sont sauvegardées dans un dossier `images/`, organisé par sous-dossier correspondant aux catégories des livres.

4/##Voici la structure des fichiers et dossiers générés par le script :
/mon-projet-de-python/ │ ├── 1-main.py 2-json_manager.py 3-player_manager.py
 # Code principal du python et d'autre fichiers  ├── requirements.txt
 # Liste des dépendances ├── README.md
 # Fichier d'explication ├── .gitignore
 # Exclusion des fichiers pycach et .venv et .idea├── controllers/
 # Dossier contenant un fichier controller.py ├── views
 # Dossier contenant un fichier menu.py ├── models
 # Dossier contenant des fichier 1-model_player 2-model_tournament 3-model-round 4-model_match |── flake8_report
 # Pour effectuer la mise en forme et le nettoyage du code