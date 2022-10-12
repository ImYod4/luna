from ._binary_tree_base import BinaryTreeBase

class LinkedBinaryTree(BinaryTreeBase):
    class _Node:
        __slots__ = '_element', '_parent', '_left', '_right'
        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._right = right
            self._left = left
    class Position(BinaryTreeBase.Position):
        def __init__(self, container, node):
            self._container = container
            self._node = node
        def element(self):
            return self._node._element
        def __eq__(self, other):
            return (type(self) is type(other)) and (self._node is other._node)
    def __init__(self):
        self._root = None
        self._size = None
    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p is not proper position type')
        if not p._container is self:
            raise ValueError('p does not belong to this container')
        if p._node is p._node._parent:
            raise ValueError('p is no longer valied')
        return p._node._element
    def __len__(self):
        return self._size
    def _make_position(self, node):
        if node is None:
            return None
        return self.Position(self, node)
    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)
    def num_childern(self, p):
        node = self._validate(p)
        count = 0
        if node._left:
            count += 1
        if node._right:
            count += 1
        return count
    def root(self):
        return self._make_position(self._root._node)
    def positions(self):
        pass
    def left(self, p):
        node = self._validate(p)
        return self._make_position(node._left)
    def right(self, p):
        node = self._validate(p)
        return self._make_position(node._right)
    def _add_root(self, e):
        if self.root() is None:
            raise ValueError('Root exists')
        self._root = self._Node(e)
        self._size += 1
        return self._make_position(self._root)
    def _add_left(self, p, e):
        node = self._validate(p)
        if not node._left is None:
            raise ValueError('Left node exists')
        node._left = self._Node(e, node)
        self._size += 1
        return self._make_position(node._left)
    def _add_right(self, p, e):
        node = self._validate(p)
        if not node._right is None:
            raise ValueError('Right node exists')
        node._right = self._Node(e, node)
        self._size += 1
        return self._make_position(node._right)
    def _replace(self, p, e):
        node = self._validate(p)
        old_value = node._element
        node._element = e
        return old_value
    def _delete(self, p):
        node = self._validate(p)
        if self.num_childern(p) == 2:
            raise ValueError('p has two children')
        child = node._left if node._left else node._right
        if not child is None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node
        return node._element
    def _attach(self, p, T1, T2):
