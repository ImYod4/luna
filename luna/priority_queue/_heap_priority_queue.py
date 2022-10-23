from ._priority_queue_base import PriorityQueueBase

class Empty(Exception):
    pass

class HeapPriorityQueue(PriorityQueueBase):
    def __init__(self):
        self._data = []
    def add(self, k, v):
        new_item = self._Item(k, v)
        self._data.append(new_item)
        self._upheap(len(self._data) - 1)
    def min(self):
        if self.is_empty():
            raise Empty('HeapPQueue is empty')
        item = self._data[0]
        return (item._key, item._value)
    def remove_min(self):
        if self.is_empty():
            raise Empty('HeapPQueue is empty')
        self._swap(0, len(self._data) - 1)
        item = self._data.pop()
        self._downheap(0)
        return (item._key, item._value)
    def _parent(self, j):
        return (j - 1) // 2
    def _left(self, j):
        return (2 * j) + 1
    def _right(self, j):
        return (2 * j) + 2
    def _has_left(self, j):
        return self._left(j) < len(self._data)
    def _has_right(self, j):
        return self._right(j) < len(self._data)
    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]
    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)
    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[j]:
                self._swap(small_child, j)
                self._downheap(small_child)
    def _show(self, name=''):
        output = name + '['
        if self.is_empty():
            return output + ']'
        counter = len(self._data)
        output = '['
        for i in range(counter):
            item = self._data[i]
            if i == counter - 1:
                output += f'{(item._key, item._value)}' + ']'
            else:
                output += f'{(item._key, item._value)}' + ', '
        return output
    def __len__(self):
        return len(self._data)
    def __str__(self):
        return self._show()
    def __repr__(self):
        return self._show('HeapPQueue')
