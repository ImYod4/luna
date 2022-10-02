from ._linked_deque_base import _LinkedDequeBase

class _Empty(Exception):
    pass

class LinkedDeque:
    def first(self):
        if self._is_empty():
            raise _Empty('deque is empty')
        return self._header._next._element
    def insert_first(self, e):
        self._insert_between(e, self._header, self._header._next)
    def insert_last(self, e):
        self._insert_between(e, self._trailer._prev, self._trailer)
    def delete_first(self):
        answer = self._delete_node(self._header._next)
        return answer
    def delete_last(self):
        answer = self._delete_node(self._trailer._prev)
        return answer
    def __str__(self):
        output = '['
        if self._is_empty():
            return output + ']'
        e = self._header._next
        for i in range(self._length):
            if i == self._length - 1:
                output += str(e._element) + ']'
            else:
                output += str(e._element) + ', '
            e = e._next
        return output
    def __repr__(self):
        output = 'LinkedDeque(['
        if self.is_empty():
            return output + '])'
        e = self._header._next
        for i in range(self._length):
            if i == self._length - 1:
                output += str(e._element) + '])'
            else:
                output += str(e._element) + ', '
            e = e._next
        return output
