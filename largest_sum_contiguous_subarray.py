# Kadane's Algorithm
#
# Given an array arr[] of size N. The task is to find the sum of the contiguous subarray within a arr[] with the
# largest sum.

def max_sub_array(nums):
    partial_sum = nums[0]
    global_max = nums[0]
    for i in range(1, len(nums)):
        partial_sum = max(partial_sum + nums[i], nums[i])
        global_max = max(global_max, partial_sum)
    return global_max

array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print(max_sub_array(array))
