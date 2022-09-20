def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr.pop()
    low = [i for i in arr if i < pivot]
    high = [i for i in arr if i > pivot]

    return quick_sort(low) + [pivot] + quick_sort(high)

arr = [21, 20, 56, 43, 3, 1, 54, 76, -87, -97, 21, 0, 2]
print(quick_sort((arr)))