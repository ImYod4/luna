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
