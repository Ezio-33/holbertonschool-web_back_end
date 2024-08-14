#!/usr/bin/env python3
"""
Module pour retourner un tuple contenant une chaîne
et le carré d'un nombre avec annotations de type.
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Retourne un tuple où le premier élément est la
    chaîne k et le second élément est le carré de v.

    Arguments:
    k -- chaîne de caractères
    v -- nombre entier ou flottant

    Return:
    Un tuple contenant la chaîne et le carré du nombre en tant que flottant.
    """
    return (k, float(v ** 2))
