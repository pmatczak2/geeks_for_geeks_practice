def rotate_array(a, d):
    n = len(a)
    trying = [a[i] for i in range(d, n)]
    for i in range(n):
        trying.append(a[i])
    return trying

arr = [1,2,3,4,5,6,7,8,9]
print(rotate_array(arr, 2))