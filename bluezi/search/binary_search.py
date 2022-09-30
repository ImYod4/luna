# binary_search.py

import random

def binary_search(S, start, end, key):
    mid = (start + end) // 2
    if end < start:
        return 'Not Found!'
    if S[mid] == key:
        return mid
    else:
        if key < S[mid]:
            return binary_search(S, start, mid - 1, key)
        else:
            return binary_search(S, mid + 1, end, key)

def main():
    a = [random.randint(0, 100) for _ in range(20)]    
    a.sort()
    print(a)
    print(binary_search(a, 0, len(a), 13))
if __name__ == '__main__':
    main()
