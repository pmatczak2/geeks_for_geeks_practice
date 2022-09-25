def sorting(array, left_index, right_index, x):

    while left_index <= right_index:
        middle = left_index + right_index - 1 // 2

        if array[middle] == x:
            return x

        elif array[middle] < x:
            left_index = middle + 1

        else:
            right_index = middle - 1

    return -1
arr = [1,2,3,4]
x = 8

print(sorting(arr, 0, len(arr) - 1, x))
