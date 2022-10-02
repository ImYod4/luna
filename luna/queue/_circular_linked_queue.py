class _Empty(Exception):
    pass

class CircularLinkedQueue:
    def __init__(self):
        self._tail = None
        self._length = 0
        self._name = self.__class__.__name__
    class _Node:
        def __init__(self, element, next_):
            self._element = element
            self._next = next_

    def __len__(self):
        return self._length
    def first(self):
        if self._is_empty():
            raise _Empty('queue is empty')
        return tail._next._element
    def _is_empty(self):
        return self._length == 0
    def enqueue(self, e):
        newest = self._Node(e, None)
        if self._is_empty():
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._length += 1
    def dequeue(self):
        if self._is_empty():
            raise _Empty('queue is empty')
        oldhead = self._tail._next
        if self._length == 1:
            self._tail = None
        else:
            self._tail._next = oldhead._next
        self._length -= 1
        return oldhead._element
    def __str__(self):
        output = '['
        if self._is_empty():
            return output + ']'
        e = self._tail._next
        for i in range(self._length):
            if i == self._length - 1:
                output += str(e._element) + ']'
            else:
                output += str(e._element) + ', '
            e = e._next
        return output
    def __repr__(self):
        output = self._name + '(['
        if self._is_empty():
            return output + '])'
        e = self._tail._next
        for i in range(self._length):
            if i == self._length - 1:
                output += str(e._element) + '])'
            else:
                output += str(e._element) + ', '
            e = e._next
        return output
