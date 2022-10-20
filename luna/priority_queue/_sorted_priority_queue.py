from luna.deque import PositionalList
from ._priority_queue_base import PriorityQueueBase

class Empty(Exception):
    pass

class SortedPriorityQueue(PriorityQueueBase):
    def __init__(self):
        self._data = PositionalList()
    def _find_min(self):
        if self.is_empty():
            raise Empty('SortedPriorityQueue is empty')
        return self._data.first()
    def min(self):
        p = self._find_min()
        item = p.element()
        return (item._key, item._value)
    def remove_min(self):
        p = self._find_min()
        item = p.element()
        self._data.delete(p)
        return (item._key, item._value)
    def add(self, k, v):
        new = self._Item(k, v)
        walk = self._data.first()
        while not (walk is None) and (new < walk.element()):
            walk = self._data.after(walk)
        if walk is None:
            self._data.add_first(new)
        else:
            self._data.add_after(walk, new)
    def __len__(self):
        return len(self._data)
    def __str__(self):
        output = '['
        if self.is_empty():
            return output + ']'
        walk = self._data.first()
        for i in range(len(self._data)):
            if self._data.after(walk) is None:
                item = walk.element()
                output += str(f'{(item._key, item._value)}') + ']'
            else:
                item = walk.element()
                output += str(f'{(item._key, item._value)}') + ', '
            walk = self._data.after(walk)
        return output
    def __repr__(self):
        output = 'S_PriorityQueue(['
        if self.is_empty():
            return output + '])'
        walk = self._data.first()
        for i in range(len(self._data)):
            if self._data.after(walk) is None:
                item = walk.element()
                output += str(f'{(item._key, item._value)}') + '])'
            else:
                item = walk.element()
                output += str(f'{(item._key, item._value)}') + ', '
            walk = self._data.after(walk)
        return output
