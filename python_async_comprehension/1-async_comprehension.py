#!/usr/bin/env python3
"""Module contenant une compréhension asynchrone."""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    Collecte 10 nombres aléatoires en utilisant une compréhension asynchrone.

    Returns:
        Une liste de 10 nombres aléatoires.
    """
    return [nombre async for nombre in async_generator()]
