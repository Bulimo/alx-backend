#!/usr/bin/env python3
"""
Module 1-simple_pagination
Implements class Server
"""
import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
            Calculate start and end indexes for a given page and page size.

            Args:
            - page (int): The current page number (1-indexed).
            - page_size (int): The number of items per page.

            Returns:
            - tuple[int, int]: A tuple containing the start and end indexes.
            """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """ Initialize the Server Class """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns data in a specific page range

        Args:
            page(int): page numberwith default value 1
            page_size(int): page size with default value 10.

        Returns:
            (list): paginated data or empty list if arguments are incorrect
        """
        assert isinstance(page, int) and page > 0
        # assert (page > 0 and page_size > 0)
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)
        if start >= len(self.dataset()):
            return []
        return self.dataset()[start: end]
