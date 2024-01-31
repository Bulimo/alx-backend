#!/usr/bin/env python3
"""
Module 100-lfu_cache
Implements class LFUCache
"""
import time
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
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
        self.__lfu_key = None
        self.__lfu_dict = {}

    def _get_frequency_sorted_dict(self):
        """ Returns a dictionary sorted by frequency """
        return dict(sorted(self.__lfu_dict.items(), key=lambda k: k[1][0]))

    def _get_least_frequent_key(self, frequency_sorted_dict):
        """
        Returns the least frequent key from a frequency-sorted dictionary
        """
        lowest_freq = frequency_sorted_dict[next(
            iter(frequency_sorted_dict))][0]
        least_freq_dict = {
            k: v for k, v in frequency_sorted_dict.items()
            if v[0] == lowest_freq}
        time_sorted_dict = dict(
            sorted(least_freq_dict.items(), key=lambda k: k[1][1]))
        return next(iter(time_sorted_dict))

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data the item value for the key
        If key or item is None, this method should not do anything.
        If the number of items is higher than BaseCaching.MAX_ITEMS:
            discard the least frequency used item (LFU algorithm)
            if more than 1 item to discard, use the LRU algorithm to discard
        """
        # if key is not None:
        #     # print("printing time_dict\n{}".format(self.__lfu_dict))
        #     if key in self.cache_data or \
        #             len(self.cache_data) < BaseCaching.MAX_ITEMS:
        #         self.cache_data[key] = item
        #     else:
        #         # created a sorted dict by frequency
        #         count_sort = dict(sorted(
        #             self.__lfu_dict.items(), key=lambda k: k[1][0]))
        #         # create a dict of those with same frequency
        #         lowest_freq = count_sort.get(next(iter(count_sort)))[0]
        #         print("lowest frequency = {}".format(lowest_freq))
        #         same_freq_dict = {}
        #         for k, v in count_sort.items():
        #             if v[0] == lowest_freq:
        #                 same_freq_dict[k] = v
        #             else:
        #                 break
        #         time_sort = dict(
        #             sorted(same_freq_dict.items(), key=lambda k: k[1][1]))
        #         self.__lfu_key = next(iter(time_sort))
        #         print("self.__lfu_key = {}".format(self.__lfu_key))
        #         # self.__lfu_key = list(sorted_dict.keys())[0]
        #         print(f"DISCARD: {self.__lfu_key}")
        #         self.cache_data.pop(self.__lfu_key)
        #         self.__lfu_dict.pop(self.__lfu_key)
        #         self.cache_data[key] = item
        #     count, ntime = self.__lfu_dict.get(key, (0, 0))
        #     count += 1
        #     ntime = time.time_ns()
        #     self.__lfu_dict[key] = (count, ntime)
        if key is not None and item is not None:
            if key in self.cache_data or \
                    len(self.cache_data) < BaseCaching.MAX_ITEMS:
                self.cache_data[key] = item
            else:
                frequency_sorted_dict = self._get_frequency_sorted_dict()
                least_frequent_key = self._get_least_frequent_key(
                    frequency_sorted_dict)

                print(f"DISCARD: {least_frequent_key}")
                self.cache_data.pop(least_frequent_key)
                self.__lfu_dict.pop(least_frequent_key)

                self.cache_data[key] = item

            count, ntime = self.__lfu_dict.get(key, (0, 0))
            count += 1
            ntime = time.time_ns()
            self.__lfu_dict[key] = (count, ntime)

    def get(self, key):
        """
        Returns the value in self.cache_data linked to key.
        If key is None or if the key doesn't exist
        in self.cache_data, return None
        """
        if key is None:
            return None
        if key in self.cache_data:
            count, ntime = self.__lfu_dict.get(key, (0, 0))
            count += 1
            ntime = time.time_ns()
            self.__lfu_dict[key] = (count, ntime)
        return self.cache_data.get(key)
