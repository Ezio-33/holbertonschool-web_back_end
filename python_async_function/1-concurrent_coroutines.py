#!/usr/bin/env python3
"""Module contenant la coroutine wait_n"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Exécute wait_random n fois avec le max_delay spécifié.

    Args:
        n (int): Nombre de fois à exécuter wait_random.
        max_delay (int): Délai maximum pour chaque exécution de wait_random.

    Return:
        List[float]: Liste des délais d'attente triés par ordre croissant.
    """
    taches = [wait_random(max_delay) for _ in range(n)]
    resultats = await asyncio.gather(*taches)
    return sorted(resultats)
