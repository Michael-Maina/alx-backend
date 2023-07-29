#!/usr/bin/env python3
"""
MRUCache class implementation
"""
from base_caching import BaseCaching
from collections import deque


class MRUCache(BaseCaching):
    """
    Defines a caching system class that implements MRU algorithm
    """
    # Queue of items accessed in dictionary using get
    KEYS_ACCESSED = deque([])

    def __init__(self):
        """
        Initializes the class
        """
        super().__init__()

    def put(self, key, item):
        """
        Assigns to the dictionary self.cache_data the item value for the key,
        checking that BaseCaching.MAX_ITEMS isn't exceeded. Else, discard first
        item following MRU algorithm
        """
        if key and item:
            if ((len(self.cache_data) == BaseCaching.MAX_ITEMS) and
            key not in self.cache_data):
                most_used_key = MRUCache.KEYS_ACCESSED.pop()
                self.cache_data.pop(most_used_key)
                print("DISCARD: {}".format(most_used_key))

            self.cache_data.update({key: item})

            if key in MRUCache.KEYS_ACCESSED:
                MRUCache.KEYS_ACCESSED.remove(key)
                MRUCache.KEYS_ACCESSED.append(key)
            else:
                MRUCache.KEYS_ACCESSED.append(key)

    def get(self, key):
        """
        Returns the value in self.cache_data linked to key
        """
        if key in MRUCache.KEYS_ACCESSED:
            MRUCache.KEYS_ACCESSED.remove(key)
            MRUCache.KEYS_ACCESSED.append(key)
        return self.cache_data.get(key)
