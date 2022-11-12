# Examples
## Array
### Dynamic Array
```python
>>> from luna.array import DynamicArray
>>> array = DynamicArray()
>>> array
DynamicArray([])
>>> for i in range(10):
...     array.append(i)
... 
>>> array
DynamicArray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> array.remove(5)
>>> array
DynamicArray([0, 1, 2, 3, 4, 6, 7, 8, 9])
>>> array.index(8)
7
>>> len(array)
9
>>> array.extend([10, 11])
>>> array
DynamicArray([0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11])
```
## Stack
### Stack with array
```python
>>> from luna.stack import ArrayStack
>>> stack = ArrayStack()
>>> for i in range(10):
...     stack.push(i)
... 
>>> stack
ArrayStack([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> stack.pop()
9
```
### Stack with linked list
```python
>>> from luna.stack import LinkedStack
>>> stack = LinkedStack()
>>> for i in range(10):
...     stack.push(i)
... 
>>> stack
LinkedStack([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> stack.pop()
9
```
## Queue
### Queue with array
```python
>>> from luna.queue import ArrayQueue
>>> queue = ArrayQueue()
>>> queue
ArrayQueue([])
>>> for i in range(10):
...     queue.enqueue(i)
... 
>>> queue
ArrayQueue([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> queue.dequeue()
0
```
### Queue with linked list
```python
>>> from luna.queue import LinkedQueue
>>> queue = LinkedQueue()
>>> queue
LinkedQueue([])
>>> for i in range(10):
...     queue.enqueue(i)
... 
>>> queue
LinkedQueue([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> queue.dequeue()
0
```
### Circular Queue with linked list
```python
>>> from luna.queue import CircularLinkedQueue
>>> q = CircularLinkedQueue()
>>> q
CircularLinkedQueue([])
>>> q.enqueue(1)
>>> q.enqueue(2)
>>> q
CircularLinkedQueue([1, 2])
>>> q.rotate()
>>> q
CircularLinkedQueue([2, 1])
```
## Deque
### Deque with array
```python
```
### Deque with linked list
```python
```
### Positional List
```python
```
## Tree
### Binary Tree with linked list
```python
```
