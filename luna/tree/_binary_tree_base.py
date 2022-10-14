from ._tree_abc import Tree

class BinaryTreeBase(Tree):
    def left(self, p):
        raise NotImplementedError('must be implemented by subclass')
    def right(self, p):
        raise NotImplementedError('must be implemented by subclass')
    def sibling(self, p):
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if self.right(parent) == p:
                return self.left(parent)
            else:
                return self.right(parent)
    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
    def positions(self):
        return self.inorder()
    def inorder(self):
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p
    def _subtree_inorder(self, p):
        if not self.left(p) is None:
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p
        
        if not self.right(p) is None:
            for other in self._subtree_inorder(self.right(p)):
                yield other

