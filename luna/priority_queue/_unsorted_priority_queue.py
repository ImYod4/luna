from ..deque import PositionalList
from ._priority_queue_base import PriorityQueueBase

class Empty(Exception):
    pass

class UnsortedPriorityQueue(PriorityQueueBase):
    def __init__(self):
        self._data = PositionalList()
    def __len__(self):
        return len(self._data)
    def _find_min(self):
        if not self.is_empty():
            min_ = self._data.first()
            walk = self._data.after(min_)
            while not walk is None:
                if walk.element() < min_.element():
                    min_ = walk
                walk = self._data.after(walk)
            return min_
        else:
            raise Empty('UnsortedPriorityQueue is empty')
    def min(self):
        p = self._find_min()
        item = p.element()
        return (item._key, item._value)
    def remove_min(self):
        p = self._find_min()
        item = p.element()
        self._data.delete(p)
        return (item._key, item._value)
    def add(self, key, value):
        self._data.add_last(self._Item(key, value))
