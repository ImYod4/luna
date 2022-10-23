from ..priority_queue import SortedPriorityQueue
from ..priority_queue import UnsortedPriorityQueue
from ..priority_queue import HeapPriorityQueue

def pq_sort(C, type_='h'):
    '''Sort a linked list based collection from luna module.'''
    if type_ == 'h':
        # Heap Sort
        p = HeapPriorityQueue()
    elif type_ == 's':
        # Selection Sort
        p = UnsortedPriorityQueue()
    elif type_ == 'i':
        # Insertion Sort
        p = SortedPriorityQueue()
    else:
        raise TypeError('invalid sort type')
    n = len(C)
    for e in range(n):
        element = C.delete(C.first())
        p.add(element, None)
    for e in range(n):
        key, _ = p.reomve_min()
        C.add_last(key)
