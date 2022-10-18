from ..queue._linked_queue import LinkedQueue

class Tree:
    class Position:
        def element(self):
            raise NotImplementedError('must be implemented by subclass')
        def __eq__(self, other):
            raise NotImplementedError('must be implemented by subclass')
        def __ne__(self, other):
            raise NotImplementedError('must be implemented by subclass')
    def root(self):
        raise NotImplementedError('must be implemented by subclass')
    def is_root(self, p):
        return self.root() == p
    def parent(self, p):
        raise NotImplementedError('must be implemented by subclass')
    def children(self, p):
        raise NotImplementedError('must be implemented by subclass')
    def num_children(self, p):
        raise NotImplementedError('must be implemented by subclass')
    def is_leaf(self, p):
        return self.num_children(p) == 0
    def positions(self):
        raise NotImplementedError('must be implemented by subclass')
    def is_empty(self):
        return len(self) == 0
    def __len__(self):
        raise NotImplementedError('must be implemented by subclass')
    def __iter__(self):
        raise NotImplementedError('must be implemented by subclass')
    def depth(self, p):
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))
    def _height1(self):
        '''An O(n ^ 2) implementation for height.'''
        return max(self.depth(c) for c in self.positions() if self.is_leaf(c))
    def _height2(self, p):
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))
    def height(self, p=None):
        if p is None:
            p = self.root()
        return self._height2(p)
    def preorder(self):
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p
    def _subtree_preorder(self, p):
        yield p
        for child in self.children(p):
            for other in self._subtree_preorder(child):
                yield other
    def postorder(self):
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p
    def _subtree_postorder(self, p):
        for child in self.children(p):
            for other in self._subtree_postorder(child):
                yield other
        yield p
    def breadth_first(self):
        if not self.is_empty():
            queue = LinkedQueue()
            queue.enqueue(self.root())
            while not queue._is_empty():
                p = queue.dequeue()
                yield p
                for child in self.children(p):
                    q.enqueue(child) 

