#!/usr/bin/env python3
"""
Module 1-fifo_cache
Implements class FIFOCache
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    Inherits from BaseCaching and is a caching system
    Implements methods:
      __init__()
        put()
        get()
    """

    def __init__(self):
        """ Initialization method of the cache class """
        super().__init__()

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data the item value for the key
        If key or item is None, this method should not do anything.
        If the number of items is higher than BaseCaching.MAX_ITEMS:
            discard the first item put in cache (FIFO algorithm)
        """
        if key is not None and item is not None:
            if key in self.cache_data or \
                    len(self.cache_data) < BaseCaching.MAX_ITEMS:
                self.cache_data[key] = item
            else:
                first_key = list(self.cache_data.keys())[0]
                print(f"DISCARD: {first_key}")
                self.cache_data.pop(first_key)
                self.cache_data[key] = item

    def get(self, key):
        """
        Returns the value in self.cache_data linked to key.
        If key is None or if the key doesn't exist
        in self.cache_data, return None
        """
        if key is not None and key in self.cache_data:
            return self.cache_data.get(key)
        return None
