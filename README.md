# chronobio-client

Client for the Python game made by @vpoulailleau
## Teams AigrisCulteurs

### How to use ?

use a venv using : 
```
python -m venv venv
```

Pattern de déplacement :

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


Lorsque nous avons un groupe d'employés sur un champ nous avons les actions suivante effectués :
- 1 employé plante légume le moins présent dans le stock de notre usine 
- 10 employés arrose le champ 

Lorsque un tracteur est appelé sur un champ c'est pour sotcker celui-ci dans l'usine. 



