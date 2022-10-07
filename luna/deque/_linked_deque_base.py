class _LinkedDequeBase:
    def __init__(self):
        self._length = 0
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header

    class _Node:
        def __init__(self, element, next_, prev):
            self._element = element
            self._next = next_
            self._prev = prev

    def __len__(self):
        return self._length
    def is_empty(self):
        return self._length == 0
    def _insert_between(self, e, left_node, right_node):
        newest = self._Node(e, None, None)
        newest._prev = left_node
        newest._next = right_node
        left_node._next = newest
        right_node._prev = newest
        self._length += 1
        return newest
    def _delete_node(self, node):
        left_node = node._prev
        right_node = node._next
        left_node._next = right_node
        right_node._prev = left_node
        self._length -= 1
        node._next = node._prev = node._element = None
        return node._element
