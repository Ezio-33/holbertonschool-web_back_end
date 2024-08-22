#!/usr/bin/env python3
"""Module contenant un générateur asynchrone."""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Générateur asynchrone qui produit 10 nombres aléatoires.

    Yields:
        float: Un nombre aléatoire entre 0 et 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)  # Attente asynchrone d'une seconde
        yield random.uniform(0, 10)  # Génère un nombre aléatoire entre 0 et 10
