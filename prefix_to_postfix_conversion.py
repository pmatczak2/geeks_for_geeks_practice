# Prefix: An expression is called the prefix expression if the operator appears in the expression before the
# operands. Simply of the form (operator operand1 operand2). Example : *+AB-CD (Infix : (A+B) * (C-D) )
#
# Postfix: An expression is called the postfix expression if the operator appears in the expression after the
# operands. Simply of the form (operand1 operand2 operator). Example : AB+CD-* (Infix : (A+B * (C-D) ) Given a Prefix
# expression, convert it into a Postfix expression. Conversion of Prefix expression directly to Postfix without going
# through the process of converting them first to Infix and then to Postfix is much better in terms of computation
# and better understanding the expression (Computers evaluate using Postfix expression).
#
# Examples:
#
# Input :  Prefix :  *+AB-CD
# Output : Postfix : AB+CD-*
# Explanation : Prefix to Infix :  (A+B) * (C-D)
#               Infix to Postfix :  AB+CD-*
#
# Input :  Prefix :  *-A/BC-/AKL
# Output : Postfix : ABC/-AK/L-*
# Explanation : Prefix to Infix :  (A-(B/C))*((A/K)-L)
#               Infix to Postfix : ABC/-AK/L-*
s = "*-A/BC-/AKL"

# Stack for storing operands
stack = []

operators = {'+', '-', '*', '/', '^'}

# Reversing the order
s = s[::-1]

# iterating through individual tokens
for i in s:

    # if token is operator
    if i in operators:

        # pop 2 elements from stack
        a = stack.pop()
        b = stack.pop()

        # concatenate them as operand1 +
        # operand2 + operator
        temp = a + b + i
        stack.append(temp)

    # else if operand
    else:
        stack.append(i)

# printing final output
print(*stack)
