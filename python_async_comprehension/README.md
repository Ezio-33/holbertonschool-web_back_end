# Python - Async Comprehension

## Ressources

**Lire ou regarder** :

- PEP 530 – Asynchronous Comprehensions
- What’s New in Python: Asynchronous Comprehensions / Generators
- Type-hints for generators

## Objectifs d'Apprentissage

À la fin de ce projet, vous devrez être capable d'expliquer à quiconque, sans l'aide de Google, comment :

- Écrire un générateur asynchrone
- Utiliser des compréhensions asynchrones
- Annoter les types des générateurs

## Exigences

**Général** :

- Éditeurs autorisés : `vi`, `vim`, `emacs`
- Tous vos fichiers seront interprétés/compilés sur Ubuntu 18.04 LTS en utilisant `python3` (version 3.7)
- Tous vos fichiers doivent se terminer par une nouvelle ligne
- La première ligne de tous vos fichiers doit être exactement `#!/usr/bin/env python3`
- Un fichier `README.md` est obligatoire à la racine du dossier du projet
- Votre code doit utiliser le style `pycodestyle` (version 2.5.x)
- La longueur de vos fichiers sera testée en utilisant `wc`
- Tous vos modules doivent avoir une documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- Toutes vos fonctions doivent avoir une documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
- Une documentation n'est pas un simple mot, c'est une phrase réelle expliquant l'objectif du module, de la classe ou de la méthode (la longueur sera vérifiée)
- Toutes vos fonctions et coroutines doivent être annotées de types.

## Tâches

### 0. Async Generator

Écrire une coroutine appelée `async_generator` qui ne prend aucun argument. La coroutine doit boucler 10 fois, chaque fois attendre asynchrone de 1 seconde, puis produire un nombre aléatoire entre 0 et 10. Utiliser le module `random`.

### 1. Async Comprehensions

Importer `async_generator` de la tâche précédente et écrire une coroutine appelée `async_comprehension` qui ne prend aucun argument. La coroutine doit collecter 10 nombres aléatoires en utilisant une compréhension asynchrone sur `async_generator`, puis retourner les 10 nombres aléatoires.

### 2. Run time for four parallel comprehensions

Importer `async_comprehension` du fichier précédent et écrire une coroutine appelée `measure_runtime` qui exécutera `async_comprehension` quatre fois en parallèle en utilisant `asyncio.gather`. `measure_runtime` doit mesurer le temps total d'exécution et le retourner.
