"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
   
   an array has a fixed size, in order to add a value to an array you have to reallocate and reorganize the entire structure
   wheras a linked list has list elements that can easily be instered or removed. The run time on a stack is much faster than an array when implementing
   push and pop. Stacks are LIFO
"""
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.append(value)

#     def pop(self):
#         if len(self.storage) == 0:
#             return None
#         return self.storage.pop()

# 2. Re-implement the Stack class, this time using the linked list implementation
#    as the underlying storage structure.
#    Make sure the Stack tests pass.
import sys
sys.path.append('../singly_linked_list/')
from singly_linked_list import Node, LinkedList

class Stack: 
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size +=1

    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.storage.remove_tail()

# a = Stack()
# a.push(5)
# a.push(10)
# a.push(12)
# print(a.size)