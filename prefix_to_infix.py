#  convert form prefix to infix ((a+b) * (c-d)) -> x + ab - cd
from collections import deque

# Convert from prefix to infix

# loop right -> left in expr:
# if symbol is operand
#     add symbol to stack
# else (symbol is operator):
#     get two topmost items in stack
#     create string "sub 1 op sub 2"
#     add resulting string to stack


def prefix_to_infix(expression):
    operators = ["^", "*", "/", "%", "+", "-"]
    expr = expression.split(" ")
    stack = deque()

    for i in range(len(expr)-1, -1, -1):
        symbol = expr[i]
        if symbol in operators:
            subexp = f"({stack.pop()} {symbol} {stack.pop()})"
            stack.append(subexp)
        else:
            stack.append(symbol)

    return stack.pop()

prefix = "* + A B - C D"
infix = prefix_to_infix(prefix)
print(infix)
