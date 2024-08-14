#!/usr/bin/env python3
"""
Module pour calculer la partie entière d'un flottant avec annotations de type.
"""


import math


def floor(n: float) -> int:
    """
    Retourne la partie entière d'un nombre flottant.

    Arguments:
    n -- nombre flottant

    Return:
    La partie entière du nombre en tant qu'entier.
    """
    return math.floor(n)
