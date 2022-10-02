# binary_search.py

def binary_search(S, start, end, *, key):
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

