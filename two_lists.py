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


arr = [1, 2, 3, 4, 5, 6]

k = 2
n = len(arr)
reverse(arr, n, k)

for i in range(0, n):
    print(arr[i], end=" ")
