#!/usr/bin/env python3
"""Module pour mesurer le temps d'exécution de
compréhensions asynchrones parallèles."""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Mesure le temps d'exécution de quatre
    compréhensions asynchrones en parallèle.

    Returns:
        Le temps total d'exécution en secondes.
    """
    debut = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    fin = time.perf_counter()
    return fin - debut
