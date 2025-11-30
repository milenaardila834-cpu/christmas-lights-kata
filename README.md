# Christmas Lights Kata – Exercice de positionnement (Simplon)

Ce dépôt contient la solution de Milena Ardila pour le **Christmas Lights Kata**, un exercice proposé dans le cadre du positionnement pour la formation en développement (Simplon).

L’objectif est de manipuler une grille de **1000 × 1000 lumières** à partir d’une liste d’instructions textuelles, et de calculer deux résultats différents.

---

## Objectifs de l’exercice

Le programme doit :

1. **Interpréter chaque instruction** (« turn on », « turn off », « toggle »).
2. **Appliquer ces instructions** sur une grille représentant des lumières.
3. **Calculer deux résultats distincts** :
   - le nombre de lumières allumées (Partie 1)
   - la luminosité totale (Partie 2)

---

## Partie 1 – Nombre de lumières allumées

Dans cette partie, chaque lumière possède un état simple :

- **True** → allumée  
- **False** → éteinte  

### Règles :
- **turn on** : allume toutes les lumières de la zone.
- **turn off** : éteint toutes les lumières.
- **toggle** : inverse l’état de chaque lumière (on ⇄ off).

Le programme compte ensuite **le total de lumières allumées**.

---

## Partie 2 – Gestion de la luminosité

Ici, les lumières n’ont plus un état binaire : elles ont un **niveau de luminosité** (un entier).

### Règles :
- **turn on** : +1 de luminosité  
- **turn off** : –1 de luminosité (mais jamais en dessous de 0)  
- **toggle** : +2 de luminosité  

Le programme calcule ensuite **la somme totale de la luminosité** de toute la grille.

---

##  Structure du code

Le fichier principal est :

- **christmas_lights.py**

Il contient :

1. **Une fonction `parse_instruction()`**  
   - analyse le texte et extrait l’action + les coordonnées.

2. **La grille de la Partie 1**  
   - représente l’état allumé/éteint.

3. **La grille de la Partie 2**  
   - représente la luminosité (entiers).

4. **Deux boucles principales**  
   - une pour calculer les lumières allumées  
   - une autre pour calculer la luminosité totale  

---

##  Contenu du dépôt

- `christmas_lights.py` – solution complète en Python  
- `README.md` – présentation du projet (ce document)

---

## Auteure

**Milena Ardila**  
Exercice de positionnement – Simplon 2025
