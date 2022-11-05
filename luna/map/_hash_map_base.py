from ._map_base import MapBase
from random import randrange

class HashMapBase(MapBase):
    def __init__(self, cap=11, p=109345121):
        self._n = 0
        self._table = cap * [ None ]
        self._prime = p
        self._scale = 1 + randrange(p - 1)
        self._shift = randrange(p - 1)
    def __len__(self):
        return self._n
    def _hash_function(self, k):
        return (self._scale * hash(k) + self._shift) % self._prime % len(self._table)
    def __getitem__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j, k)
    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)
        if self._n > len(self._table) // 2:
            self._resize(2 * len(self._table) - 1)
    def __delitem__(self, k):
        j = self._hash_function(k) 
        self._bucket_delitem(j, k)
        self._n -= 1
    def _resize(self, c):
        old = list(self.items())
        self._table = c * [ None ]
        self._n = 0
        for (k, v) in old:
            self[k] = v
