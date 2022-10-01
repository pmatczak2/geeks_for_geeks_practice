# Given an array of integers where each element represents the max number of steps that can be made forward from that element.
# Write a function to return the minimum number of jumps to reach the end of the array (starting from the first element).
# If an element is 0, they cannot move through that element. If the end isn’t reachable, return -1.

# Input: arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}
# Output: 3 (1-> 3 -> 9 -> 9)
# Explanation: Jump from 1st element
# to 2nd element as there is only 1 step,
# now there are three options 5, 8 or 9.
# If 8 or 9 is chosen then the end node 9
# can be reached. So 3 jumps are made.
def min_jumps(arr, n):
    if n <= 1:
        return 0

    if arr[0] == 0:
        return -1

    max_range = arr[0]
    step = arr[0]
    jump = arr[0]

    for i in range(1, n):
        if i == n-1:
            return jump

        max_range = max(max_range, i + arr[i])
        step -= 1
        if step == 0:
            jump += 1
            step = max_range - i

        if i >= max_range:
            return -1
    return -1

arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
size = len(arr)
print(f"Minimum number of jumps to reach end is {min_jumps(arr, size)}")
