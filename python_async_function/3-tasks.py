#!/usr/bin/env python3
"""Module contenant la fonction task_wait_random"""


import asyncio
from typing import Any


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Crée une tâche asyncio à partir de la coroutine wait_random.

    Args:
        max_delay (int): Délai maximum pour wait_random.

    Returns:
        asyncio.Task: Tâche asyncio créée.
    """
    return asyncio.create_task(wait_random(max_delay))
