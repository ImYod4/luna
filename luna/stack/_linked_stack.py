class _Empty(Exception):
    pass

class LinkedStack:
    def __init__(self):
        self._head = None
        self._length = 0
        self._name = self.__class__.__name__

    class _Node:
        __slots__ = '_element', '_next'
        
        def __init__(self, element, next_):
            self._element = element
            self._next = next_

    def __len__(self):
        return self._length
    def push(self, e):
        newest = self._Node(e, self._head)
        self._head = newest
        self._length += 1
    def pop(self):
        if self._is_empty():
            raise _Empty('stack is empty!')
        answer = self._head._element
        self._head = self._head._next
        self._length -= 1
        return answer
    def _is_empty(self):
        return self._length == 0
    def __str__(self):
        output = '['
        if self._is_empty():
            return output + ']'
        e = self._head
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
        e = self._head
        for i in range(self._length):
            if i == self._length - 1:
                output += str(e._element) + '])'
            else:
                output += str(e._element) + ', '
            e = e._next
        return output
