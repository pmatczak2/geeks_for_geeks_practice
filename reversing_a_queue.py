# Give an algorithm for reversing a queue Q. Only the following standard operations are allowed on queue.
#
# enqueue(x): Add an item x to the rear of the queue.
# dequeue(): Remove an item from the front of the queue.
# empty(): Checks if a queue is empty or not.
# The task is to reverse the queue.
#
# Examples:
#
# Input: Q = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Output: Q = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]

from collections import deque

def reversqueue(queue):
    stack = []

    while (queue):
        stack.append(queue[0])
        queue.popleft()

    while len(stack) != 0:
        queue.append(stack[-1])
        stack.pop()





if __name__ == '__main__':
    queue = deque([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    reversqueue(queue)
    print(queue)