# Given an array and a number K where K is smaller than the size of the array. Find the K’th the largest  element in the
# given array. Given that all array elements are distinct.
#
# Examples:
#
# Input: arr[] = {7, 10, 4, 3, 20, 15}, K = 3
# Output: 7
#
# Input: arr[] = {7, 10, 4, 3, 20, 15}, K = 4
# Output: 10

import heapq

def find_kth_largest(array, k):
    return heapq.nsmallest(k, array)[-1]


if __name__ == '__main__':

    array = [7, 10, 4, 3, 20, 15]
    k = 4
    print(find_kth_largest(array,k))
