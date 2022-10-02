class _DequeBase:
    def __init__(self):
        self._length = 0
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._name = self.__class__.__name__

    class _Node:
        def __init__(self, element, next_, prev):
            self._element = element
            self._next = next_
            self._prev = prev

    def __len__(self):
        return self._length
    def _is_empty(self):
        return self._length == 0
    def _insert_between(self, e, left_node, right_node):
        newest = self._Node(e, None, None)
        newest._prev = left_node
        newest._next = right_node
        left_node._next = newest
        right_node._prev = newest
        self._size += 1
    def _delete_node(self, node):
        left_node = node._prev
        right_node = node._next
        left_node._next = right_node
        right_node._prev = left_node
        self._size -= 1
        return node._element
