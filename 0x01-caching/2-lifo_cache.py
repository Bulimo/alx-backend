#!/usr/bin/env python3
"""
Module 2-lifo_cache
Implements class LIFOCache
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
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
        self.__last_key = None

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data the item value for the key
        If key or item is None, this method should not do anything.
        If the number of items is higher than BaseCaching.MAX_ITEMS:
            discard the last item put in cache (LIFO algorithm)
        """
        if key is not None:
            if key in self.cache_data or \
                    len(self.cache_data) < BaseCaching.MAX_ITEMS:
                self.cache_data[key] = item
            else:
                print(f"DISCARD: {self.__last_key}")
                self.cache_data.pop(self.__last_key)
                self.cache_data[key] = item
            self.__last_key = key

    def get(self, key):
        """
        Returns the value in self.cache_data linked to key.
        If key is None or if the key doesn't exist
        in self.cache_data, return None
        """
        if key is None:
            return None
        return self.cache_data.get(key)
