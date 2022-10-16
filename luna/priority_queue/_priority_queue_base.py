
class PriorityQueueBase:
    class _Item:
        __slots__ = '_key', '_value'
        
        def __init__(self, key, value):
            self._key = key
            self._value = value
        def __lt__(self, other):
            return self._key < other._key
    def __len__(self):
        raise NotImplementedError('must be implemented by subclass')
    def is_empty(self):
        return len(self) == 0
