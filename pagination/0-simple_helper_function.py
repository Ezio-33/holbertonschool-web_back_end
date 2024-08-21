#!/usr/bin/env python3
"""Module contenant la fonction helper pour la pagination"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calcule les index de début et de fin pour une page donnée.

    Args:
        page (int): Le numéro de la page (commençant à 1).
        page_size (int): Le nombre d'éléments par page.

    Returns:
        Tuple[int, int]: Un tuple contenant l'index de début et l'index de fin.
    """
    debut = (page - 1) * page_size
    fin = page * page_size
    return (debut, fin)
