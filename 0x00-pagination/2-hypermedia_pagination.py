#!/usr/bin/env python3
"""
Defines index range function
"""
import csv
import math
from typing import Dict, List, Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    Returns a tuple of size two containing a start index and an end index
    for a range of indexes to return in a list for those particular
    pagination parameters
    """
    start_idx = (page_size * page) - page_size
    end_idx = (page_size * page)
    return (start_idx, end_idx)


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
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
        Returns a list of lists with the data from each row in a CSV file
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        all_rows = self.dataset()
        try:
            idx_range = index_range(page, page_size)
            rows = [all_rows[i] for i in range(idx_range[0], idx_range[1])]
            return rows
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Returns a dictionary with data on pagination
        """
        data = self.get_page(page, page_size)
        next_page = page + 1 if data else None
        prev_page = page - 1 if page > 1 else None
        total_pages = math.ceil(len(self.dataset()) / page_size)

        hyper_dict = {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }

        return hyper_dict
