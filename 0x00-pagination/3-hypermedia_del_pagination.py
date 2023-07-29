#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

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

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Dataset indexed by sorting position, starting at 0
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
        Returns a dictionary with data on deletion resilient pagination
        """
        # data_len = len(self.dataset())
        # max_index = data_len - 1
        # next_index = min(index + page_size, max_index + 1)

        # assert index < max_index

        # dataset = [self.indexed_dataset().get(i, None)
        #            for i in range(index, next_index)]
        # result = {}
        # result["index"] = index
        # result["data"] = dataset
        # result["page_size"] = page_size
        # result["next_index"] = next_index

        # return result

        if index is None:
            index = 0

        assert isinstance(index, int)
        assert 0 <= index < len(self.indexed_dataset())
        assert isinstance(page_size, int) and page_size > 0

        data = []
        next_index = index + page_size

        for i in range(index, next_index):
            if self.indexed_dataset().get(i):
                data.append(self.indexed_dataset()[i])
            else:
                i += 1
                next_index += 1

        result = {
            "index": index,
            "data": data,
            "page_size": page_size,
            "next_index": next_index
            }
        
        return result
