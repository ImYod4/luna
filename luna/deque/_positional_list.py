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
        if not isinstance(p, self._Position):
            raise TypeError('p must be proper position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        return p._node
    def first(self):
        return self._make_position(self._header._next)
    def last(self):
        return self._make_position(self._trailer._prev)
    def before(self, p):
        node = self._validate(p)
        return self._make_position(node._prev)
    def after(self, p):
        node = self._validate(p)
        return self._make_position(node._next)
    def _make_position(self, node):
        if node is self._header or node is self._trailer:
            return None
        return self._Position(self, node)
    def _insert_between(self, e, left_node, right_node):
        super()._insert_between(e, left_node, right_node)
    def add_first(self, e):
        self._insert_between(e, self._header, self._header._next)
    def add_last(self, e):
        self._insert_between(e, self._trailer._prev, self._trailer)
    def add_before(self, p, e):
        node = self._validate(p)
        self._insert_between(e, node._prev, node)
    def add_after(self, p, e):
        node = self._validate(p)
        self._insert_between(e, node, node._next)
    def delete(self, p):
        node = self._validate(p)
        self._delete_node(node)
    def replace(self, p, e):
        original = self._validate(p)
        old_value = original._element
        old_value._element = e
        return old_value
    def delete_first(self):
        first_p = self.first()
        self.delete(first_p)
    def delete_last(self):
        last_p = self.last()
        self.delete(last_p)
    def sort(self):
        # insertion sort
        if len(self) > 1:
            marker = self.first()
            while marker != self.last():
                pivot = self.after(marker)
                value = pivot.element()
                if value > marker.element():
                    marker = pivot
                else:
                    walk = marker
                    while walk != self.first() and self.before(walk).element() > value:
                        walk = self.before(walk)
                    self.delete(pivot)
                    self.add_before(walk, value)
    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)
    def __str__(self):
        output = '('
        if self.is_empty():
            return output + ')'
        cursor = self.first()
        while cursor is not None:
            if self.after(cursor) is None:
                output += str(cursor.element()) + ')'
            else:
                output += str(cursor.element()) + ' -> '
            cursor = self.after(cursor)
        return output
    def __repr__(self):
        return str(self)
