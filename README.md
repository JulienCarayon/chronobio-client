<div id="top"></div>

[![Contributors][contributors-shield]][contributors-url]
[![Stargazers][stars-shield]][stars-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url-1]
[![LinkedIn][linkedin-shield]][linkedin-url-2]
[![LinkedIn][linkedin-shield]][linkedin-url-3]

# Teams AigrisCulteurs
###### Client for the Python game made by @vpoulailleau
<div align="center">
  </br>
  <img src="Documents/Image/aigriculteur.png" alt=" 3 BG aigrisculteurs" width="600">
  </br></br>
</div>

> Petit jeu: Trouvez les 5 soupes !!!!

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table des matières</summary>
  <ol>
    <li>
      <a href="#travail-en-local">Travail en local</a>
      <ul>
	<li><a href="#prérequis">Prérequis</a></li>
        <li><a href="#lancer-la-simulation">Lancer la simulation</a></li>
        <li><a href="#stopper-la-simulation">Stopper la simulation</a></li>
      </ul>
    </li>
    <li>
      <a href="#mise-en-place-des-tests">Mise en place des tests</a>
      <ul>
        <li><a href="#installer-pytest">Installer pytest</a></li>
	<li><a href="#utilisation-dans-le-projet">Utilisation dans le projet</a></li>
        <li><a href="#lancer-les-tests">Lancer les tests</a></li>
      </ul>
    </li>
    <li><a href="#mise-en-place-de-pré-commit">Mise en place de Pré-commit</a></li>
      <ul>
        <li><a href="#installation-et-ajout-au-projet">Installation et ajout au projet</a></li>
        <li><a href="#tests-pré-commit">Tests pré-commit</a></li>
      </ul>
    <li><a href="#github-actions">GitHub Actions</a></li>
    <li><a href="#théorie-vs-pratique">Théorie VS Pratique</a></li>
      <ul>
        <li><a href="#gestion-des-déplacements">Gestion des déplacements</a></li>
      </ul>
    <li><a href="#best-scores-ever">Best scores ever</a></li>
  </ol>
</details>

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

- se placer dans le dossier chronobio et lancer le script **killal.py** : ```python killal.py```

<p align="right"><a href="#top">:point_up_2:</a></p>

## Mise en place des tests
Travail en intégration continue à l'aide de pytest.

- [Pytest documentation](https://docs.pytest.org/en/7.2.x/)
- [Pytest-cov documentation](https://pypi.org/project/pytest-cov/)

### Installer pytest
Effectuer la commande suivante : ```pip install -r requierements-test.txt```

Contenu du fichier **requierements-test.txt**:
```python
flake8==3.9.0
pytest==7.2.2
pytest-cov==4.0.0
```

### Utilisation dans le projet
Nous travaillons avec un fichier **pyproject.toml** nous permettant de spécifier les versions des outils utilisées dans le projet
###### Contenu du fichier pyproject.toml : [pyproject.toml](./pyproject.toml)

### Lancer les tests
Avec l'intégration du fichier **pyproject.toml**, il suffit de lancer la commande ```pytest``` pour effectuer les tests et générer un rapport.

<p align="right"><a href="#top">:point_up_2:</a></p>

## Mise en place de Pré-commit
Des pré-commit sont disponibles au sein de projet, dans le but de vérifier certains éléments avant la mise à jour sur le projet au global et bloquer ou non les commit collaborateurs.

- [Pre-commit documentation](https://pre-commit.com/)

### Installation et ajout au projet
Utilisation d'un fichier **.pre-commit-config.yaml** de configuration disponible à la racine du repository. Ce fichier décrit quels repository et hook sont installés pour les vérifications de pré-commit.

###### Contenu du fichier .pre-commit-config.yaml : [.pre-commit-config.yaml](./.pre-commit-config.yaml)

### Tests pré-commit
Commande pour run les pre-commit sur l'ensemble des fichiers sans effectuer de commit : ```pre-commit run --all-files```
<p align="right"><a href="#top">:point_up_2:</a></p>

## GitHub Actions
Ajouts de GitHub Action permettant de lancer des scripts de linter (ex : *flake8*), ainsi que d'intégration continu (ex : *pytest*).
- [flake8 documentation](https://flake8.pycqa.org/en/latest/)

<p align="right"><a href="#top">:point_up_2:</a></p>

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
- Embauche le 29 du mois --> employés présent le jour 0 sur les champs

### Gestion des licenciement
Pour la gestion des licenciements nous avons fait une simulation sur plusieurs durées tels que 6 mois, 7 mois, 1an, 2ans...
Au final lors de cette simulation de coût nous en avons déduit que le cout de revient optimal est une gestion de licenciement sur une durée de ```1 an et 3 mois```.
###### Se référer au document suivant : [Documents/Gestion_Strategie_Licenciement](./Documents/Gestion_Strategie_Licenciement.xlsx)

<p align="right"><a href="#top">:point_up_2:</a></p>

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
Soit pour une production de soupe de 5 légumes une consommation de ```21 200 légumes``` nous avons donc une nécessité de 8 employés afin d'exploité au mieux le rendement de l'usine :

| nb employés |     production soupe 1 jour     |    Production soupe 1 mois    |
|-------------|---------------------------------|-------------------------------|
|      7      |               700               |              21000            |
|      8      |               800               |              24000            |


Nous avons calculé le coût de revient réel pour une production de soupe de 5 légumes avec 8 employés à l'usine.
En théorie nous pouvons donc obtenir au maximum sans intempérie ```8 633 109```
###### Se référer au document suivant : [Documents/Benefices_Production_Soupe_Théorique](./Documents/Benefices_Production_Soupe_Théorique.xlsx)

<p align="right"><a href="#top">:point_up_2:</a></p>

## Best scores ever
- ***Mode Local*** : ```8 534 943```
- ***Mode Réseau*** : ```8 156 643```
> En suivant la stratégie précédemment décrite

<p align="right"><a href="#top">:point_up_2:</a></p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/JulienCarayon/chronobio-client/graphs/contributors
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/JulienCarayon/chronobio-client/stargazers
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url-1]: https://www.linkedin.com/in/dorian-fournier/
[linkedin-url-2]: https://www.linkedin.com/in/julien-carayon/
[linkedin-url-3]: https://www.linkedin.com/in/jordan-clement-68b39019a/

