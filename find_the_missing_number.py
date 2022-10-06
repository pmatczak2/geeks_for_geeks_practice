# Given an array arr[] of size N-1 with integers in the range of [1, N], the task is to find the missing number from
# the first N integers.
#
# Note: There are no duplicates in the list.
#
# Examples:
# Input: arr[] = {1, 2, 4, 6, 3, 7, 8}, N = 8
# Output: 5
# Explanation: The missing number between 1 and 8 is 5
# Input: arr[] = {1, 2, 3, 5}, N = 5
# Output: 4
# Explanation: The missing number between 1 and 5 is 4

def get_missing_number(a, n):
    i, total = 0, 1

    for i in range(2, n + 2):
        total += i
        total -= a[i - 2]
    return total


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 7, 8, 9, 10]
    N = len(arr)

    print(get_missing_number(arr, N))
