# Find duplicates in O(n) time and O(1) extra space | Set 1
# Find duplicates in O(n) time and O(1) extra space | Set 1
# Input : n = 7 and array[] = {1, 2, 3, 6, 3, 6, 1}
# Output: 1, 3, 6
#
# Explanation: The numbers 1 , 3 and 6 appears more
# than once in the array.
num_ray = [0, 4, 3, 2, 7, 8, 2, 3, 1]
arr_size = len(num_ray)

for i in range(arr_size):
    x = num_ray[i] % arr_size
    num_ray[x] = num_ray[x] + arr_size

for i in range(arr_size):
    if num_ray[i] >= arr_size * 2:
        print(num_ray[i])

# Approach: The basic idea is to use a HashMap to solve the problem. But there is a catch, the numbers in the array
# are from 0 to n-1, and the input array has length n. So, the input array can be used as a HashMap. While Traversing
# the array, if an element ‘a’ is encountered then increase the value of a%n‘th element by n. The frequency can be
# retrieved by dividing the a % n’th element by n. Algorithm: Traverse the given array from start to end. For every
# element in the array increment the arr[i]%n‘th element by n. Now traverse the array again and print all those
# indexes i for which arr[i]/n is greater than 1. Which guarantees that the number n has been added to that index
# This approach works because all elements are in the range from 0 to n-1 and arr[i] would be greater than n only if
# a value “i” has appeared more than once.
