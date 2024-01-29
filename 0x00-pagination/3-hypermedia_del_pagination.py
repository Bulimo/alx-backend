#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Retrieve information for the dataset based on index and page size.

        Args:
        - index (int):  the current start index of the return page
        - page_size (int): The number of items per page (default is 10).

        Returns:
        - (dict): { index, next_index, page_size, data }
        """
        assert index is None or (isinstance(
            index, int) and index >= 0)
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.indexed_dataset()
        total_items = len(dataset)

        if index is None:
            index = 0
        else:
            assert index < total_items, "Index is out of range."

        start_index = index
        # Update internal dataset representation after deletion
        while start_index not in dataset:
            # print("Incrementing by 1")
            start_index += 1
        end_index = start_index + page_size
        # Ensure end index is within bounds
        end_index = min(end_index, total_items - 1)

        next_index = end_index if end_index < total_items - 1 else None
        # print("Start Index = {}".format(start_index))
        # print("dataset[start_index] = {}".format(dataset[start_index]))

        return {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': [dataset[i] for i in range(start_index, end_index)]
        }
