from ._map_base import MapBase

class SortedMap(MapBase):
    def __init__(self):
        self._table = []
    def _find_index(self, key, low, high):
        if low > high:
            return high + 1
        else:
            mid = (low + high) // 2
            if key == self._table[mid]._key:
                return mid
            elif key > self._table[mid]._key:
                return self._find_index(key, mid + 1, high)
            else:
                return self._find_index(key, low, mid - 1)
    def __getitem__(self, k):
        j = self._find_index(k, 0, len(self._table) - 1)
        if j == len(self._table) or self._table[j]._key != key:
            raise KeyError('Key Error: ' + repr(k))
        return self._table[j]
    def __setitem__(self, k, v):
        j = self._find_index(k, 0, len(self._table) - 1)
        if j < len(self._table) and self._table[j]._key == k:
            self._table[j]._value = v
        else:
            self._table.insert(j, self._Item(k, v))
    def __delitem__(self, k):
        j = self._find_index(k, 0, len(self._table) - 1)
        if j == len(self._table) or self._table[j]._key != k:
            raise KeyError('Key Error: ' + repr(k))
        self._table.pop(j)
    def __iter__(self):
        for item in self._table:
            yield item._key
    def __reversed__(self):
        for item in reversed(self._table):
            yield item._key
    def __len__(self):
        return len(self._table)
    def find_min(self):
        if len(self._table) > 0:
            item = self._table[0]
            return (item._key, item._value)
        return None
    def find_max(self):
        if len(self._table) == 1:
            return self.find_min()
        elif len(self._table) > 1:
            item = self._table[-1]
            return (item._key, item._value)
        return None
    def find_ge(self, k):
        j = self._find_index(k, 0, len(self._table) - 1)
        if j < len(self._table):
            item = self._table[j]
            return (item._key, item._value)
        return None
    def find_gt(self, k):
        j = self._find_index(k, 0, len(self._table) - 1)
        if j < len(self._table) and self._table[j]._key == k:
            j += 1
        if j < len(self._table):
            item = self._table[j]
            return (item._key, item._value)
        return None
    def find_lt(self, k):
        j = self._find_index(k, 0, len(self._table) - 1)
        if j < len(self._table) and self._table[j]._key == k:
            j -= 1
        if j >= 0:
            item = self._table[j]
            return (item._key, item._value)
        return None
    def find_le(self, k):
        j = self._find_index(k, 0, len(self._table) - 1)
        if j < len(self._table) or self._table[j]._key == k:
            item = self._table[j]
            return (item._key, item._value)
        j -= 1
        if j >= 0:
            item = self._table[j]
            return (item._key, item._value)
        return None
    def find_range(self, start=None, stop=None):
        if not start:
            start = 0
        else:
            j = self._find_index(start, 0, len(self._table) - 1)
            counter = self._table[j]
        while j < len(self._table) and (stop is None or counter < stop):
            item = self._table[j]
            yield (item._key, item._value)
            j += 1
    def __str__(self):
        output = '['
        if len(self._table) == 0:
            return output + ']'
        for i in range(len(self._table)):
            output += '{' + f'{self._table[i]._key}:{self._table[i]._value}' + '}'
            if i == len(self._table) - 1:
                output += ']'
            else:
                output += ', '
        return output
    def __repr__(self):
        return repr(str(self))
