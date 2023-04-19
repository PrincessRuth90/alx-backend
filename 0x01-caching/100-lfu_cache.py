#!/usr/bin/python3
"""a class LFUCache that inherits from BaseCaching and is a caching system"""


from enum import Enum
from heapq import heappush, heappop
from itertools import count

BaseCaching = __import__("base_caching").BaseCaching


class HeapItemStatus(Enum):
    """Status of the heap item status"""
    Active = 1
    Inactive = 2


class LFUCache(BaseCaching):
    """LFUCache method"""

    def __init__(self):
        """initialize"""
        self.load = []
        self.round = {}
        self.counting = count()

    def put(self, key, item):
        """put function"""
        if key and item:
            if key in self.cache_data:
                self.add(key)
            else:
                if self.full():
                    self.remove()
                self.add_heap(key)
            self.cache_data[key] = item

    def get(self, key):
        """get function"""
        if key in self.cache_data:
            self.add(key)
            return self.cache_data.get(key)

    def full(self):
        """Check if the no is full"""
        len(self.cache_data) >= self.MAX_ITEMS

    def remove(self):
        """remove the item"""
        while self.heap:
            _, __, item, status = heappop(self.heap)
            if status == HeapItemStatus.Active:
                print("DISCARD: " + str(item))
                del self.cache_data[item]
                return

    def add(self, key):
        """add"""
        entry = self.round[key]
        entry[-1] = HeapItemStatus.Inactive
        self.add(key, entry[0])

    def add_heap(self, key, count=0):
        """add to the heap"""
        entry = [1 + count, next(self.counter), key, HeapItemStatus.Active]
        self.map[key] = entry
        heappush(self.heap, entry)
