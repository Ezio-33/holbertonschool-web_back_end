#!/usr/bin/env python3
"""Module contenant la coroutine wait_random"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Attend pendant un délai aléatoire et retourne ce délai.

    Args:
        max_delay (int): Le délai maximum en secondes. Par défaut 10.

    Return:
        float: Le temps d'attente en secondes.
    """
    delai = random.uniform(0, max_delay)
    await asyncio.sleep(delai)
    return delai
