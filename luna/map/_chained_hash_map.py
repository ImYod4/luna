from ._hash_map_base import HashMapBase
from ._unsorted_map import UnsortedMap

class ChainedHashMap(HashMapBase):
    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))
        return bucket[k]
    def _bucket_setitem(self, j, k, v):
        if self._table[j] is None:
            self._table[j] = UnsortedMap()
        old_size = len(self._table[j])
        self._table[j][k] = v
        if old_size < len(self._table[j]):
            self._n += 1
    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))
        del bucket[k]
    def __iter__(self):
        for bucket in self._table:
            if not bucket is None:
                for key in bucket:
                    yield key
    def __str__(self):
        output = '{'
        if len(self) == 0:
            return output + '}'
        for i in range(len(self._table)):
            if self._table[i] is None:
                continue
            bucket = self._table[i]
            for (k, v) in bucket.items():
                output += f'{k}: {v}' + ', '
        output = output.strip(', ')
        return output + '}'
    def __repr__(self):
        return repr(str(self))
