# Annotations de Type en Python

## Objectifs d'apprentissage

À la fin de ce projet, tu devrais être capable d'expliquer à quiconque, sans l'aide de Google :

- Les annotations de type en Python 3
- Comment utiliser les annotations de type pour spécifier les signatures de fonction et les types de variables
- Le concept de _duck typing_
- Comment valider ton code avec `mypy`

## Exigences

- Éditeurs autorisés : `vi`, `vim`, `emacs`
- Tous tes fichiers seront interprétés/compilés sur Ubuntu 20.04 LTS en utilisant `python3` (version 3.9)
- Tous tes fichiers doivent se terminer par une nouvelle ligne
- La première ligne de tous tes fichiers doit être exactement `#!/usr/bin/env python3`
- Un fichier `README.md`, à la racine du dossier du projet, est obligatoire
- Ton code doit utiliser le style `pycodestyle` (version 2.5.)
- Tous tes fichiers doivent être exécutables
- La longueur de tes fichiers sera testée en utilisant `wc`
- Tous tes modules doivent avoir une documentation
- Toutes tes classes doivent avoir une documentation
- Toutes tes fonctions (à l'intérieur et à l'extérieur d'une classe) doivent avoir une documentation

## Ressources

**À lire ou regarder :**

- [Documentation sur le typage en Python 3](https://docs.python.org/3/library/typing.html)
- [Feuille de triche `mypy`](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)

## Tâches

1. **Annotations de base - addition**

   - Écrire une fonction annotée `add` qui prend deux flottants `a` et `b` en arguments et retourne leur somme.

2. **Annotations de base - concaténation**

   - Écrire une fonction annotée `concat` qui prend deux chaînes `str1` et `str2` et retourne leur concaténation.

3. **Annotations de base - partie entière**

   - Écrire une fonction annotée `floor` qui prend un flottant `n` et retourne sa partie entière.

4. **Annotations de base - conversion en chaîne**

   - Écrire une fonction annotée `to_str` qui prend un flottant `n` et retourne sa représentation en chaîne.

5. **Définir des variables**

   - Définir et annoter les variables suivantes : `a` (int), `pi` (float), `i_understand_annotations` (bool), `school` (str).

6. **Types complexes - liste de flottants**

   - Écrire une fonction annotée `sum_list` qui prend une liste de flottants et retourne leur somme.

7. **Types complexes - liste mixte**

   - Écrire une fonction annotée `sum_mixed_list` qui prend une liste de nombres entiers et flottants et retourne leur somme.

8. **Types complexes - chaîne et int/float en tuple**

   - Écrire une fonction annotée `to_kv` qui prend une chaîne `k` et un int ou un float `v` et retourne un tuple.

9. **Types complexes - fonctions**

   - Écrire une fonction annotée `make_multiplier` qui prend un flottant `multiplier` et retourne une fonction qui multiplie un flottant par `multiplier`.

10. **Duck typing d'un objet itérable**
    - Annoter une fonction `element_length` qui retourne une liste de tuples contenant un élément et sa longueur.
