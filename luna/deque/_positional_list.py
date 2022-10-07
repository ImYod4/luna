from ._linked_deque_base import _LinkedDequeBase

class PositionalList(_LinkedDequeBase):

    class _Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node
        def element(self):
            return self._node._element
        def __eq__(self, other):
            return type(self) is type(other) and self._node is other._node
        def __ne__(self, other):
            return not (self == other)
    def _validate(self, p):
        if not isinstance(p, self._Positon):
            raise TypeError('p must be proper position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        return p._node
    def first(self):
        pass
    def last(self):
        pass
    def before(self, p):
        pass
    def after(self, p):
        pass
    def _insert_between(self, e, left_node, right_node):
        pass
    def add_first(self, p, e):
        pass
    def add_last(self, p, e):
        pass
    def add_before(self, p, e):
        pass
    def add_after(self, p, e):
        pass
    def delete(self, p):
        pass
    def replace(self, p, e):
        pass
    def __iter__(self):
        pass
    def __str__(self):
        pass
    def __repr__(self):
        pass
