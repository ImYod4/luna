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
    def childern(self, p):
        raise NotImplementedError('must be implemented by subclass')
    def num_childern(self, p):
        raise NotImplementedError('must be implemented by subclass')
    def is_leaf(self, p):
        raise NotImplementedError('must be implemented by subclass')
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
            return 1 + max(self._height2(c) for c in self.childern(p))
    def height(self, p=None):
        if p is None:
            p = self.root()
        return self._height2(p)
