# Welcome to luna

**luna is a python package for datastructure and algorithms.**

Advantages of luna:
- written %100 in python3
- zero dependency
- clear coding for educational use
- easy to use!
- very good performance
- ...

## how to install

1. run `git clone https://github.com/ImYod4/luna.git`
2. cd to luna directory
3. install build with `pip3 install --upgrade build`
4. run `python3 -m build`
5. run `pip3 install dist/<version>.tar.gz`

# Examples
## Stack
### Stack with array
```python
from luna.stack import ArrayStack

stack = ArrayStack()

print(stack)

for i in range(10):
	stack.push(i)

print(stack)

print(stack.pop())
```
### Stack with linked list
```python
from luna.stack import LinkedStack

stack = LinkedStack()

print(stack)

for i in range(10):
	stack.push(i)

print(stack)

print(stack.pop())
```
