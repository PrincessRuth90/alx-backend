#!/usr/bin/env python3
"""a class LFUCache that inherits from BaseCaching and is a caching system"""

from enum import Enum
from heapq import heappush, heappop
from itertools import count

BaseCaching = __import__("base_caching").BaseCaching


class HeapItemStatus(Enum):
    """Status of the heap"""
    ACTIVE = 1
    INACTIVE = 2


class LFUCache(BaseCaching):
    """LFUCache function"""

    def __init__(self):
        """initialize"""
        super().__init__()
        self.heap = []
        self.map = {}
        self.counter = count()

    def put(self, key, item):
        """put function"""
        if key and item:
            if key in self.cache_data:
                self.rehydrate(key)
            else:
                if self.is_full():
                    self.evict()
                self.add_to_heap(key)
            self.cache_data[key] = item

    def get(self, key):
        """get function"""
        if key in self.cache_data:
            self.rehydrate(key)
            return self.cache_data.get(key)

    def is_full(self):
        """check if its full"""
        return len(self.cache_data) >= self.MAX_ITEMS

    def evict(self):
        """check if evicted"""
        while self.heap:
            _, __, item, status = heappop(self.heap)
            if status == HeapItemStatus.ACTIVE:
                print("DISCARD: " + str(item))
                del self.cache_data[item]
                return

    def rehydrate(self, key):
        """ Marks item as inactive"""
        entry = self.map[key]
        entry[-1] = HeapItemStatus.INACTIVE
        self.add_to_heap(key, entry[0])

    def add_to_heap(self, key, count=0):
        """add to the heal"""
        entry = [1 + count, next(self.counter), key, HeapItemStatus.ACTIVE]
        self.map[key] = entry
        heappush(self.heap, entry)
