# Given an array of integers arr[] of size N and an integer, the task is to rotate the array elements to the left by d positions.
# Input:
# arr[] = {1, 2, 3, 4, 5, 6, 7}, d = 2
# Output: 3 4 5 6 7 1 2
#
# Input: arr[] = {3, 4, 5, 6, 7, 1, 2}, d=2
# Output: 5 6 7 1 2 3 4

def rotate_array(L, d):
    k = L.index(d)
    new_list = L[k+1:]+L[:k+1]
    return new_list

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
d = 3
arr = rotate_array(arr, d)
for i in arr:
    print(i, end=" ")
