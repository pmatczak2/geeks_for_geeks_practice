# Given a sequence arr[] of size n, Write a function int equilibrium(int[] arr, int n) that returns an equilibrium
# index (if any) or -1 if no equilibrium index exists.
#
# The equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of
# elements at higher indexes.
#
# Examples:
#
# Input: A[] = {-7, 1, 5, 2, -4, 3, 0}
# Output: 3
# 3 is an equilibrium index, because:
# A[0] + A[1] + A[2] = A[4] + A[5] + A[6]

# Initialize leftsum  as 0
# Get the total sum of the array as sum
# Iterate through the array and for each index i, do the following:
# Update the sum to get the right sum.
# sum = sum – arr[i]
# The sum is now the right sum
# If leftsum is equal to the sum, then return the current index.
# update left sum for the next iteration.
# leftsum = leftsum + arr[i]
# Return -1
# If we come out of the loop without returning then there is no equilibrium index

def equilibrium(arr):
    total_sum = sum(arr)
    leftsum = 0
    for i, num in enumerate(arr):
        total_sum -= num

        if leftsum == total_sum:
            return i
        leftsum += num

    return -1


if __name__ == "__main__":
    arr = [-7, 1, 5, 2, -4, 3, 0]

    # Function call
    print('First equilibrium index is ',
          equilibrium(arr))