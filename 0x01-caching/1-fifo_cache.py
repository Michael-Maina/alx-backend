#!/usr/bin/env python3
"""
FIFOCache class implementation
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Defines a caching system class that implements FIFO algorithm
    """
    def __init__(self):
        """
        Initializes the class
        """
        super().__init__()

    def put(self, key, item):
        """
        Assigns to the dictionary self.cache_data the item value for the key,
        checking that BaseCaching.MAX_ITEMS isn't exceeded. Else, discard first
        item following FIFO algorithm
        """
        if key is None or item is None:
            pass

        self.cache_data.update({key: item})

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = list(self.cache_data.keys())[0]
            self.cache_data.pop(first_key)
            print("DISCARD: {}".format(first_key))

    def get(self, key):
        """
        Returns the value in self.cache_data linked to key
        """
        return self.cache_data.get(key)
