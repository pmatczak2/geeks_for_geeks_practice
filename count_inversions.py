# Inversion Count for an array indicates – how far (or close) the array is from being sorted. If the array is already
# sorted, then the inversion count is 0, but if the array is sorted in reverse order, the inversion count is the
# maximum.
#
# Given an array a[]. The task is to find the inversion count of a[]. Where two elements a[i] and a[j] form an
# inversion if a[i] > a[j] and i < j.
#
# Examples:
#
# Input: arr[] = {8, 4, 2, 1}
# Output: 6
# Explanation: Given array has six inversions: (8, 4), (4, 2), (8, 2), (8, 1), (4, 1), (2, 1).
#
def getInvCount(arr, n):

    inv_count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (arr[i] > arr[j]):
                inv_count += 1

    return inv_count
arr = [1, 20, 6, 4, 5]
n = len(arr)
print("Number of inversions are",
      getInvCount(arr, n))