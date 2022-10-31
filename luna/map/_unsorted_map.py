from ._map_base import MapBase

class UnsortedMap(MapBase):
    def __init__(self):
        self._table = []
    def __len__(self):
        return len(self._table)
    def __setitem__(self, k, v):
        for item in self._table:
            if item._key == k:
                item._key = k
                item._value = v
                return
        self._table.append(self._Item(k, v))
    def __getitem__(self, k):
        for item in self._table:
            if item._key == k:
                return item._value
        raise KeyError('Key Not Found: ' + repr(k))
    def __delitem__(self, k):
        for i in range(len(self._table)):
            if k == self._table[i]._key:
                self._table.pop(i)
                return
        raise KeyError('Key Not Found: ' + repr(k))
    def __iter__(self):
        for item in self._table:
            yield item._key
    def __str__(self):
        if len(self._table) == 0:
            return '{}'
        output = '{'
        for i in range(len(self._table)):
            if i == len(self._table) - 1:
                output += repr(self._table[i]._key) + ': ' + str(self._table[i]._value) + '}'
            else:
                output += repr(self._table[i]._key) + ': ' + str(self._table[i]._value) + ', '
        return output
    def __repr__(self):
        return str(self)
