#!/usr/bin/env python3
"""Module contenant la fonction measure_time"""

import time
import asyncio
from typing import List


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Mesure le temps moyen d'exécution de wait_n.

    Args:
        n (int): Nombre de fois à exécuter wait_random.
        max_delay (int): Délai maximum pour chaque exécution de wait_random.

    Return:
        float: Temps moyen d'exécution par appel.
    """
    debut = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    fin = time.perf_counter()

    temps_total = fin - debut
    return temps_total / n
