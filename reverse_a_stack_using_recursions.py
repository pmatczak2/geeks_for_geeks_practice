# Write a program to reverse a stack using recursion, without using any loop.

# Example:
#
# Input: st = [1, 5, 3, 2, 4]
# Output:[4, 2, 3, 5, 1]
# Explanation: After reversing the stack [1, 5, 3, 2, 4] becomes [4, 2, 3, 5, 1].

class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items ==[]
    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def display(self):
        for data in reversed(self.items):
            print(data)

def insert_at_bottom(s, data):
    if s.is_empty():
        s.push(data)
    else:
        popped = s.pop()
        insert_at_bottom(s, data)
        s.push(popped)


def reverse_stack(s):
    if not s.is_empty():
        popped = s.pop()
        reverse_stack(s)
        insert_at_bottom(s, popped)

s = Stack()
data_list = [1, 5, 3, 2, 4]
for data in data_list:
    s.push(data)

print('The stack:')
s.display()
reverse_stack(s)
print('After reversing:')
s.display()
