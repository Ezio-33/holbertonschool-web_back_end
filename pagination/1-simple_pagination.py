#!/usr/bin/env python3
"""Module pour la pagination simple"""

import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """Calcule les index de début et de fin pour une page donnée."""
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


class Server:
    """Classe Server pour paginer une base de données de prénoms populaires."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Dataset mis en cache"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retourne la page appropriée du dataset."""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.dataset()
        try:
            start, end = index_range(page, page_size)
            return dataset[start:end]
        except IndexError:
            return []
