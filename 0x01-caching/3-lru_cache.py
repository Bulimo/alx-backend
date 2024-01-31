#!/usr/bin/env python3
"""
Module 3-lru_cache
Implements class LRUCache
"""
import time
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
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
        self.__lru_key = None
        self.__time_dict = {}
        self.order_of_access = []

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data the item value for the key
        If key or item is None, this method should not do anything.
        If the number of items is higher than BaseCaching.MAX_ITEMS:
            discard the least item put in cache (LRU algorithm)
        """
        # if key is not None and item is not None:
        #     # print("printing time_dict\n{}".format(self.__time_dict))
        #     if key in self.cache_data or \
        #             len(self.cache_data) < BaseCaching.MAX_ITEMS:
        #         self.cache_data[key] = item
        #     else:
        #         # created a sorted dict by time tag
        #         sorted_dict = list(sorted(
        #             self.__time_dict.items(), key=lambda k: k[1]))
        #         # self.__lru_key = next(iter(sorted_dict))
        #         self.__lru_key = sorted_dict[0][0][0]
        #         # print("self.__lru_key = {}".format(self.__lru_key))
        #         print(f"DISCARD: {self.__lru_key}")
        #         self.cache_data.pop(self.__lru_key)
        #         self.__time_dict.pop(self.__lru_key)
        #         self.cache_data[key] = item
        #     self.__time_dict[key] = time.time_ns()
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Discard the least recently used item (LRU algorithm)
                lru_key = self.order_of_access.pop(0)
                if key not in self.cache_data:
                    print("DISCARD: {}".format(lru_key))
                del self.cache_data[lru_key]

            self.cache_data[key] = item
            self.order_of_access.append(key)

    def get(self, key):
        """
        Returns the value in self.cache_data linked to key.
        If key is None or if the key doesn't exist
        in self.cache_data, return None
        """
        # if key is None:
        #     return None
        # if key in self.cache_data:
        #     self.__time_dict[key] = time.time_ns()
        # return self.cache_data.get(key)
        if key is not None and key in self.cache_data:
            # Update order_of_access to indicate recent use
            self.order_of_access.remove(key)
            self.order_of_access.append(key)
            return self.cache_data.get(key)
        return None
