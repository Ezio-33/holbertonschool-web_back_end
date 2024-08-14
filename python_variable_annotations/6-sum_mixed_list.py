#!/usr/bin/env python3
"""
Module pour calculer la somme d'une liste mixte
d'entiers et de flottants avec annotations de type.
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Retourne la somme d'une liste de nombres entiers et flottants.

    Arguments:
    mxd_lst -- liste de nombres entiers et flottants

    Return:
    La somme des nombres en tant que flottant.
    """
    return sum(mxd_lst)
