# Given an array arr[] of non-negative integers and an integer sum, find a subarray that adds to a given sum.
#
# # Note: There may be more than one subarray with sum as the given sum, print first such subarray.
# Input: arr[] = {1, 4, 20, 3, 10, 5}, sum = 33
# Output: Sum found between indexes 2 and 4
# Explanation: Sum of elements between indices 2 and 4 is 20 + 3 + 10 = 33

def sub_array_sum(arr, n, sum_):
    current_sum = arr[0]
    start = 0
    i = 1

    while i <= n:

        while current_sum > sum_:
            current_sum = current_sum - arr[start]
            start += 1

        if current_sum == sum_:
            print(f"sum is in index {start} and {i - 1}")
            return 1

        if i < n:
            current_sum = current_sum + arr[i]
        i += 1

    print("No subarray found")
    return 0
arr = [15, 2, 4, 8, 9, 5, 10, 23]
n = len(arr)
sum_ = 23

sub_array_sum(arr, n, sum_)
