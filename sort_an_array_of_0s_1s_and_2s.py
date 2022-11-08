# Given an array A[] consisting of only 0s, 1s, and 2s. The task is to write a function that sorts the given array.
# The functions should put all 0s first, then all 1s and all 2s in last.
#
# This problem is also the same as the famous “Dutch National Flag problem”. The problem was proposed by Edsger
# Dijkstra. The problem is as follows:
#
# def sort_array(arr):
#     return sorted(arr)
#


def sort_array(a, arr_size):
    low = 0
    high = arr_size - 1
    mid = 0

    while mid <= high:

        if a[mid] == 0:
            a[low], a[mid] = a[mid], a[low]
            low += 1
            mid += 1

        elif a[mid] == 1:
            mid += 1

        else:
            a[mid], a[high] = a[high], a[mid]
            high -= 1
    return a

array = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
array_size = len(array)
print(sort_array(array, array_size))