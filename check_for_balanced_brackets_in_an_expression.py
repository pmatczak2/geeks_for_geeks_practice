# Given an expression string exp, write a program to examine whether the pairs and the orders of “{“, “}”, “(“, “)”,
# “[“, “]” are correct in the given expression.
#
# Example:
#
# Input: exp = “[()]{}{[()()]()}”
# Output: Balanced
# Explanation: all the brackets are well-formed
#
# Input: exp = “[(])”
# Output: Not Balanced
# Explanation: 1 and 4 brackets are not balanced because
# there is a closing ‘]’ before the closing ‘(‘
# Time Complexity: O(N), Iteration over the string of size N one time.
# Auxiliary Space: O(N) for stack.

def is_balanced(string_is):
    stack = []

    for char in string_is:
        if char in ["(", "{", "["]:
            stack.append(char)
        else:
            if not stack:
                return False
            current_cha = stack.pop()
            if current_cha == "(":
                if char != ")":
                    return False
            if current_cha == "{":
                if char != "}":
                    return False
            if current_cha == "[":
                if char != "]":
                    return False
    if stack:
        return False
    return True


if __name__ == "__main__":
    string_is = "{()}[]"

    if is_balanced(string_is):
        print("Balanced")
    else:
        print("Not Balanced")
