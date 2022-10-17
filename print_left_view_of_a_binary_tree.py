# Print Left View of a Binary Tree
# Input :
#                  1
#                /   \
#               2     3
#              / \     \
#             4   5     6
# Output : 1 2 4


# (Using Queue): In this method, level order traversal based solution is discussed. If we observe carefully, we will see
# that our main task is to print the left most node of every level. So, we will do a level order traversal on the tree and
# print the leftmost node at every level. Below is the implementation of above approach:
# Below is the implementation of the above idea-


# Python3 program to print left view of
# Binary Tree
# Print Left View of a Binary Tree
# Binary Tree Node
""" utility that allocates a newNode
with the given key """


class NewNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def print_left_side(root):
    if not root:
        return

    queue = [root]

    while len(queue):
        n = len(queue)

        for i in range(1, n + 1):
            temp = queue[0]
            queue.pop(0)

            if i == 1:
                print(temp.data, end=" ")

            if temp.left is not None:
                queue.append(temp.left)

            if temp.right is not None:
                queue.append(temp.right)

if __name__ == "__main__":
    root = NewNode(10)
    root.left = NewNode(2)
    root.right = NewNode(3)
    root.left.left = NewNode(7)
    root.left.right = NewNode(8)
    root.right.right = NewNode(15)
    root.right.left = NewNode(12)
    root.right.right.left = NewNode(14)
    print_left_side(root)


