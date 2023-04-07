# Teams AigrisCulteurs 
###### Client for the Python game made by @vpoulailleau
<div align="center">
  </br>
  <img src="Documents/Image/aigriculteur.png" alt="Game name" width="600">
  </br></br>
</div>

> Petit jeu: Trouvez les 5 soupes !!!!

## Travail en local

### Prérequis 
1. installer un environnement virtuel : ```python -m venv venv```
2. avoir un esprit compétitif, et être un BG aigrisculteur

### Lancer la simulation
1. se placer dans le dossier chronobio
2. activer un environnement virtuel : ```source venv/bin/activate``` 
> l'indication ```(venv)``` apparaît à gauche du prompt
3. lancer le script 'competition.sh' :  ```./competition.sh```

### Stopper la simulation
- attendre la fin de la simulation

ou

- se placer dans le dossier chronobio et lancer le script 'killal.py' : ```python killal.py```

## Mise en place des tests

De l'integration continue à été effectuée sur les codes sources du projet afin de s'assurer 
#### Intaller pytest sur votre machine
Travailler sur l'environnement virtuel : ```python -m venv venv```

#### Installation de pytest :
```pip install -u pytest```

## Pré-commit
Des pre-commit sont disponibles au sein de projet, dans le but de vérifier certains éléments avant la mise à jour sur le projet au global.

## Théorie VS Pratique

### Théorie :
Lors du dévellopement du projet nous devions prendre en compte plusieurs éléments :
- Achat champ
- Achat tracteur
- Gestion des employés 
- Gestion des licenciement 
- Gestion des déplacements
- Gestion production soupe 

### Gestion champ/tracteur
Nous avons opté pour un achat des 5 champ soit une dépense de 50 000€ et un achat de 4 tracteurs soit 120 000€ lors du jour 0. 

### Gestion des employés
Pour la gestion des employés nous avons opté pour la stratégie suivante:
- Licenciement le 29 du mois 
- Embauche le 29 du mois --> employés présent le jour 0

### Gestion des licenciement
Pour la gestion des licenciements nous avons fait une simulation sur plusieurs durées tels que 6 mois, 7 mois, 1an, 2ans...
Au final lors de cette simulation de coût nous en avons déduit que le cout de revient optimal est une gestion de licenciement sur une durée de ```1 an et 3 mois```.
###### Pour voir le cacul merci de se référer au document suivant : [Documents/Gestion_Strategie_Licenciement](./Documents/Gestion_Strategie_Licenciement.xlsx)

### Gestion des déplacements
#### Pattern stratégie

| Jours |     Ferme     |    Champ 1    |    Champ 2    |    Champ 3    |    Champ 4    |    Champ 5    |     Usine     |  Disponibilité  |
|-------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|-----------------|
|  J0   |       X       |  33 employés  |       X       |       X       |       X       |       X       |       X       |                 |
|       |  4 tracteurs  |       X       |       X       |       X       |       X       |       X       |       X       |                 |
|  J1   | 8 cuisiniers  |       X       |  33 employés  |       X       |       X       |       X       |       X       |                 |
|       |  3 tracteurs  | Tracteur  N°1 |       X       |       X       |       X       |       X       |       X       |                 |
|  J2   |  0  employés  |       X       |  11 employés  |  22 employés  |       X       |       X       |       X       |                 |
|       |  2 tracteurs  |       X       | Tracteur  N°2 |       X       |       X       |       X       |       X       |                 |
|  J3   |  0  employés  |  11 employés  |       X       |       X       |  22 employés  |       X       |       X       |  Tracteur N°1   |
|       |  1 tracteurs  |       X       |       X       | Tracteur  N°3 |       X       |       X       |       X       |                 |
|  J4   |  0  employés  |       X       |  11 employés  |  11 employés  |       X       |  11 employés  |       X       |  Tracteur N°2   |
|       |  0 tracteurs  | Tracteur  N°1 |       X       |       X       | Tracteur  N°4 |       X       |       X       |                 |
|  J5   |  0  employés  |       X       |       X       |       X       |  11 employés  |  11 employés  |       X       |                 |
|       |  0 tracteurs  |       X       | Tracteur  N°2 | Tracteur  N°3 |       X       | Tracteur  N°4 |       X       |                 |
|  J6   |  0  employés  |       X       |       X       |  11 employés  |       X       |  11 employés  |  8 cuisiniers |                 |
|       |  0 tracteurs  |       X       |       X       |       X       | Tracteur  N°3 |       X       |       X       |                 |
|  J7   |  0  employés  |  11 employés  |       X       |       X       |  11 employés  |  11 employés  |  8 cuisiniers |  Tracteur N°1   |
|       |  0 tracteurs  |       X       |       X       | Tracteur  N°3 |       X       | Tracteur  N°4 |       X       |                 |
|  J8   |  0  employés  |       X       |  11 employés  |  11 employés  |       X       |  11 employés  |  8 cuisiniers |  Tracteur N°2   |
|       |  0 tracteurs  | Tracteur  N°1 |       X       |       X       | Tracteur  N°3 |       X       |       X       |                 |
|  J9   |  0  employés  |       X       |       X       |       X       |  11 employés  |  11 employés  |  8 cuisiniers |                 |
|       |  0 tracteurs  |       X       | Tracteur  N°2 | Tracteur  N°3 |       X       | Tracteur  N°4 |       X       |                 |
|  J10  |  0  employés  |       X       |       X       |  11 employés  |       X       |  11 employés  |  8 cuisiniers |                 |
|       |  0 tracteurs  |       X       |       X       |       X       |       X       |       X       |       X       |                 |
|  J11  |  0  employés  |  11 employés  |       X       |       X       |  11 employés  |  11 employés  |  8 cuisiniers |  Tracteur N°1   |
|       |  0 tracteurs  |       X       |       X       | Tracteur  N°3 |       X       | Tracteur  N°4 |       X       |                 |
|  J12  |  0  employés  |       X       |  11 employés  |  11 employés  |       X       |  11 employés  |  8 cuisiniers |  Tracteur N°2   |
|       |  0 tracteurs  | Tracteur  N°1 |       X       |       X       |       X       |       X       |       X       |                 |
|  J13  |  0  employés  |       X       |       X       |       X       |  11 employés  |  11 employés  |  8 cuisiniers |                 |
|       |  0 tracteurs  |       X       | Tracteur  N°2 | Tracteur  N°3 |       X       | Tracteur  N°4 |       X       |                 |

#### Explication pattern
Lorsque nous avons un groupe d'employés sur un champ nous avons les actions suivantes effectuées :
- 1 employé plante le légume le moins présent dans le stock de notre usine 
- 10 employés arrose le champ 

Lorsqu'un tracteur est appelé sur un champ c'est pour stocker celui-ci dans l'usine. 
Les 8 cuisiniers produisent en permanence des soupes.  

### Gestion de la production soupe
Dans un premier temps nous avons déterminer le nombre de légumes qu'on arrive à stocker au moins. Afin de pouvoir déterminer au mieux le nombre d'meployé nécessaire.
Pour notre groupe nous produisons :```106 000 légumes```
Soit pour une production de soupe de 5 légumes une consommation de ```21 200 légumes``` nous avons donc une nécessité de 8 employés :

| nb employés |     production soupe 1 jour     |    Production soupe 1 mois    | 
|-------------|---------------------------------|-------------------------------|
|      8      |               800               |              24000            |
		

Nous avons calculé le coût de revient réel pour une production de soupe de 5 légumes avec 8 employés à l'usine.
En théorie nous pouvons donc obtenir au maximum sans intempérie ```8 633 109€```
###### Pour voir le cacul merci de se référer au document suivant : [Documents/Benefices_Production_Soupe_Théorique](./Documents/Benefices_Production_Soupe_Théorique.xlsx)
