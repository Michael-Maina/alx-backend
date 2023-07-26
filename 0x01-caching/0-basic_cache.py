#!/usr/bin/env python3
"""
BasicCache class implementation
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache extends BaseCaching class by defining the put and get methods
    """
    def put(self, key, item):
        """
        Assigns to the dictionary self.cache_data the item value for the key
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data.update({key: item})

    def get(self, key):
        """
        Returns the value in self.cache_data linked to key
        """
        return self.cache_data.get(key)
