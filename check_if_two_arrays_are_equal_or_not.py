# Given two arrays, arr1 and arr2 of equal length N, the task is to find if the given arrays are equal or not.
#
# Two arrays are said to be equal if:
#
# both of them contain the same set of elements,
# arrangements (or permutations) of elements might/might not be same.
# If there are repetitions, then counts of repeated elements must also be the same for two arrays to be equal.
# Examples:
#
# Input: arr1[] = {1, 2, 5, 4, 0}, arr2[] = {2, 4, 5, 0, 1}
# Output: Yes

def are_equal(array1, array2, length1, length2):
    if length1 != length2:
        return False

    array1.sort()
    array2.sort()

    for i in range(0, length1):
        if array1[i] != array2[i]:
            return False

    return True


if __name__ == "__main__":
    arr1 = [3, 5, 2, 5, 2]
    arr2 = [2, 3, 5, 5, 2]
    n = len(arr1)
    m = len(arr2)

    if (are_equal(arr1, arr2, n, m)):
        print("Yes")
    else:
        print("No")
