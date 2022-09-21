def sorting(arr, left, right, x):
    while left <= right:

        mid_point = left + right - 1 // 2

        if arr[mid_point] == x:
            return mid_point

        elif arr[mid_point] < x:
            left = mid_point + 1

        else:
            right = mid_point - 1
    return -1

arr = [1,2,3,4]
x = 10

result = sorting(arr, 0, len(arr)-1, x)

if result != -1:
    print(f"Element is in idex {result}")
else:
    print("Elemnt is not present")

