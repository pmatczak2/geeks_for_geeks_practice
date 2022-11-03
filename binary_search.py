# Problem: Given a sorted array arr[] of n elements, write a function to search a given element x in arr[] and return
# the index of x in the array.
#
#                  Consider array is 0 base index.
#
# Examples:
#
# Input: arr[] = {10, 20, 30, 50, 60, 80, 110, 130, 140, 170}, x = 110
# Output: 6
# Explanation: Element x is present at index 6.




def binary_search(array, left_index, right_index, x):

    while left_index <= right_index:
        middle = left_index + right_index - 1 // 2

        if array[middle] == x:
            return x

        elif array[middle] < x:
            left_index = middle + 1

        else:
            right_index = middle - 1

    return -1
arr = [2, 3, 4, 10, 40, 45]
x = 45

result = binary_search(arr, 0, len(arr) - 1, x)

if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element in not present in array")