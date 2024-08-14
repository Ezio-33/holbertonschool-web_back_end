#!/usr/bin/env python3
"""
Module pour annoter une fonction qui retourne la longueur
des éléments d'un itérable avec annotations de type.
"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Retourne une liste de tuples contenant chaque
    élément de lst et sa longueur.

    Arguments:
    lst -- itérable de séquences

    Return:
    Une liste de tuples où chaque tuple contient un élément
    de lst et sa longueur.
    """
    return [(i, len(i)) for i in lst]
