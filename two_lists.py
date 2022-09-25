# Given an array arr[] of positive integers of size N. Reverse every sub-array group of size K.
# Note: If at any instance, there are no more subarrays of size greater than or equal to K, then reverse the last subarray
# (irrespective of its size).
# Input:
# N = 5, K = 3
# arr[] = {1,2,3,4,5}
# Output: 3 2 1 5 4
# Explanation: First group consists of elements
# 1, 2, 3. Second group consists of 4,5.



def reverse(array, n, k):
    i = 0
    while i < n:
        left = i

        right = min(i + k - 1, n - 1)

        while left < right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1

        i += k


arr = [1, 2, 3, 4, 5]

k = 3
n = len(arr)
reverse(arr, n, k)

for i in range(0, n):
    print(arr[i], end=" ")
