# Input: str = “2 3 1 * + 9 -“
# Output: -4
# Explanation:
#
# Scan 2, it’s a number, so push it to stack. Stack contains ‘2’ Scan 3, again a number, push it to stack,
# stack now contains ‘2 3’ (from bottom to top) Scan 1, again a number, push it to stack, stack now contains ‘2 3 1’
# Scan *, it’s an operator, pop two operands from stack, apply the * operator on operands, we get 3*1 which results
# in 3. We push the result 3 to stack. The stack now becomes ‘2 3’. Scan +, it’s an operator, pop two operands from
# stack, apply the + operator on operands, we get 3 + 2 which results in 5. We push the result 5 to stack. The stack
# now becomes ‘5’. Scan 9, it’s a number, so we push it to the stack. The stack now becomes ‘5 9’. Scan -,
# it’s an operator, pop two operands from stack, apply the – operator on operands, we get 5 – 9 which results in -4.
# We push the result -4 to the stack. The stack now becomes ‘-4’. There are no more elements to scan, we return the
# top element from the stack (which is the only element left in a stack). Input: str = “100 200 + 2 / 5 * 7 +”
# Output: 757

# Python program to evaluate value of a postfix expression

# Class to convert the expression

class Stack1:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

    def evaluation(self, exp):
        for i in exp:
            if i.isdigit():
                self.push(i)
            else:
                var2= self.pop()
                var1 = self.pop()

                self.push(str(eval(var1 + i + var2)))
        return int(self.pop())


exp = "34+5*6-"

s = Stack1()
s.push("a")
print(s.is_empty())
print(s.peek())
s.pop()
print(s.size())
print(f"postfix evaluation {s.evaluation(exp)}")
