#!/usr/bin/env python3
"""Module pour la pagination résistante aux suppressions"""

import csv
import math
from typing import List, Dict


class Server:
    """Classe Server pour paginer une base de données de prénoms populaires."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Dataset mis en cache"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexé par position de tri, commençant à 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Retourne les informations de pagination
        résistante aux suppressions"""
        assert index is None or (isinstance(index, int) and index >= 0)
        assert isinstance(page_size, int) and page_size > 0

        indexed_data = self.indexed_dataset()
        data_length = len(indexed_data)

        if index is None:
            index = 0

        assert index < data_length

        next_index = index
        data = []

        for _ in range(page_size):
            while next_index < data_length and next_index not in indexed_data:
                next_index += 1
            if next_index == data_length:
                break
            data.append(indexed_data[next_index])
            next_index += 1

        return {
            'index': index,
            'next_index': next_index,
            'page_size': len(data),
            'data': data
        }
