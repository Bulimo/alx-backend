#!/usr/bin/env python3
""" Module 0-simple_helper_function """

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indexes for a given page and page size.

    Args:
    - page (int): The current page number (1-indexed).
    - page_size (int): The number of items per page.

    Returns:
    - tuple[int, int]: A tuple containing the start and end indexes.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)
