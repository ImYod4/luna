from ._hash_map_base import HashMapBase

class ProbeHashMap(HashMapBase):
    _AVAIL = object()

    def _is_available(self, j):
        item = self._table[j]
        return item is None or item is ProbeHashMap._AVAIL
    def _find_slot(self, j, k):
        while True:
            if self._is_available(j):
                if self._table[j] is None:
                    return (False, None)
            elif k == self._table[j]._key:
                return (True, j)
            j = (j + 1) % len(self._table)
    def _bucket_setitem(self, j, k, v):
        found, s = self._find_slot(j, k)
        if not found:
            self._table[j] = self._Item(k, v)
            self._n += 1
        else:
            self._table[s]._value = v
    def _bucket_getitem(self, j, k):
        found, s = self._find_slot(j, k)
        if found:
            return self._table[s]._value
        raise KeyError('Key Error: ' + repr(k))
    def _bucket_delitem(self, j, k):
        found, s = self._find_slot(j, k)
        if found:
            self._table[s] = ProbeHashMap._AVAIL
        else:
            raise KeyError('Key Error: ' + repr(k))
    def __iter__(self):
        for i in range(len(self._table)):
            if not self._is_available(i):
                yield self._table[i]._key
    def __str__(self):
        output = '['
        if self._n == 0:
            return output + ']'
        i = 0
        while i < len(self._table):
            if not self._is_available(i):
                output += '{' + f'{self._table[i]._key}:{self._table[i]._value}' + '}, '
            i += 1
        output = output.rstrip(', ')
        return output + ']'
    def __repr__(self):
        return repr(str(self))
