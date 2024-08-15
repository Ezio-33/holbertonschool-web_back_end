#!/usr/bin/env python3
"""Module contenant la coroutine task_wait_n"""


import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Exécute task_wait_random n fois avec le max_delay spécifié.

    Args:
        n (int): Nombre de fois à exécuter task_wait_random.
        max_delay (int): Délai maximum pour chaque exécution de
        task_wait_random.

    Returns:
        List[float]: Liste des délais d'attente triés par ordre croissant.
    """
    taches = [task_wait_random(max_delay) for _ in range(n)]
    resultats = await asyncio.gather(*taches)
    return sorted(resultats)
