# Gestion Stock Munitions

TP dans le cadre de l'apprentissage de python

>[!info] Initialisation
>exécuter le fichier init_projet.py

>[!info] requirements "auto"
>``pip freeze > requirements.txt``
## Fonctionnalités

- Ajouter
- Enlever
- Lister
- Alerte
- Prévision

- gestion des erreurs
- gestion des logs

## Biblio conseillées 

- sys
- loggin
- date
- math

## Data

### munitions : 
ID ; Type ; qte 
### Logs
  date au format ISO 8601


## Roadmap/TODO

- [x] générer des données:
	- [x] fonction pour générer des données de test
- [ ] Gestion des données:
	- [x] vérifier le fichier au lancement du programme
	- [x] fonction pour charger les données + gestion simple des erreurs
	- [x] Fonction pour écrire les données dans le fichiers + gestion des erreurs
- [ ] FONCTIONS PRINCIPALES
	- [ ] Ajouter
		- [x] fonction
		- [ ] gestion erreurs
		- [ ] log
	- [ ] Retirer
		- [ ] fonction
		- [ ] gestion erreurs
		- [ ] log
	- [ ] Lister
		- [ ]  fonction
		- [ ] gestion erreurs
		- [ ] log
	- [ ] Alerte
		- [ ]  fonction
		- [ ] gestion erreurs
		- [ ] log
	- [ ] Prévision
		- [ ] fonction
		- [ ] gestion erreurs
		- [ ] log
- [ ] FONCTIONS ANNEXES
	- [ ] Exporter les données
- [ ] gestion des Logs
- [ ] gérer les paramètres de l'appli (rassembler dans un json? )
	- mode verbose
	- paramètres pour générer le jeu de données de test (TOTAL_STOCK + MAX_QUANTITY_PER_ITEM)
- [ ] 