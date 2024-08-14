#!/usr/bin/env python3
"""
Module pour créer une fonction qui multiplie un flottant par un multiplicateur donné avec annotations de type.
"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Retourne une fonction qui multiplie un flottant par le multiplicateur donné.

    Arguments:
    multiplier -- le multiplicateur à utiliser

    Return:
    Une fonction qui prend un flottant et retourne le produit avec le multiplicateur.
    """
    def multiplier_function(value: float) -> float:
        """
        Multiplie le nombre donné par le multiplicateur.

        Arguments:
        value -- le nombre à multiplier

        Return:
        Le produit du nombre et du multiplicateur.
        """
        return value * multiplier

    return multiplier_function
