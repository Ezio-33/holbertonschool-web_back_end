#!/usr/bin/env python3
"""
Module pour calculer la somme d'une liste de flottants avec annotations de type.
"""

from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    Retourne la somme d'une liste de nombres flottants.

    Arguments:
    input_list -- liste de nombres flottants

    Return:
    La somme des nombres en tant que flottant.
    """
    return sum(input_list)
