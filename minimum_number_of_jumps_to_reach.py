#Given an array of integers where each element represents the max number of steps that can be made forward from that element.
# Write a function to return the minimum number of jumps to reach the end of the array (starting from the first element).
# If an element is 0, they cannot move through that element. If the end isn’t reachable, return -1.

# Input: arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}
# Output: 3 (1-> 3 -> 9 -> 9)
# Explanation: Jump from 1st element
# to 2nd element as there is only 1 step,
# now there are three options 5, 8 or 9.
# If 8 or 9 is chosen then the end node 9
# can be reached. So 3 jumps are made.


def min_jumps(arr, start_index, end_index):
    if end_index == start_index:
        return 0

    if arr[start_index] == 0:
        return float('inf')

    min = float('inf')
    for i in range(start_index + 1, end_index + 1):
        if i < start_index + arr[start_index] + 1:
            jumps = min_jumps(arr, i, end_index)
            if jumps != float('inf') and jumps + 1 < min:
                min = jumps + 1


arr = [1, 3, 6, 3, 2, 3, 6, 8, 9, 5]
n = len(arr)
print("Minimum number of jumps to reach end is", min_jumps(arr, 0, n-1))