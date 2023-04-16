#!/usr/bin/env python3
""" A function named index_range that takes two integer arguments
"""


def index_range(page: int, page_size: int) -> tuple:
    """ return a tuple of size two containing a start index and an end index
    """

    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
