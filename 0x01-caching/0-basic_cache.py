#!/usr/bin/env python3
"""
Module 0-basic_cache
Implements BasicCache Class that inherits from BaseCaching
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Class to implement a Basic caching system
    Has methods:
      __init__()
      put()
      get()
    """

    def __init__(self):
        """ Initialization method of the cache class """
        super().__init__()

    def put(self, key, item):
        """
        Assigns to the dictionary self.cache_data the item value for the key.
        If key or item is None, this method should not do anything.
        """
        if key is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Returns the value in self.cache_data linked to key.
        If key is None or if the key doesn't exist
        in self.cache_data, return None
        """
        if key is None:
            return None
        return self.cache_data.get(key)
