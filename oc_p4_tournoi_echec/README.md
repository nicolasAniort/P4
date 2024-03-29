# OpenClassrooms: Projet 4: Gestion d'un tournoi d'echec
Ce programme a été créé dans le cadre du projet 4 d'OpenClassrooms. 
Il s'agit d'un gestionnaire de tournois d'échecs pour une association , en mode console.

## Installation:
Commencez tout d'abord par installer Python.
Lancez ensuite la console, placez vous dans le dossier de votre choix puis clonez ce repository:
```
git clone 
```
Placez vous dans le dossier OC_P4_tournoi_echec, puis créez un nouvel environnement virtuel:
```
python -m venv env
```
Ensuite, activez-le.
Windows:
```
env\scripts\activate.bat
```
Linux:
```
source env/bin/activate
```
Il ne reste plus qu'à installer les packages requis:
```
pip install -r requirements.txt
```
## Lancement:
Vous pouvez enfin lancer le script:
```
python main.py
```
## Test de conformité PEP8 avec Flake8:
Tapez la ligne de commande suivante pour générer le rapport
```
flake8 --format=html --htmldir=flake-report --exclude=env --max-line-length=119
```