# Find the majority element in the array. A majority element in an array A[] of size n is an element that appears
# more than n/2 times (and hence there is at most one such element).
#
# Examples :
#
# Input : {3, 3, 4, 2, 4, 4, 2, 4, 4}
# Output : 4
# Explanation: The frequency of 4 is 5 which is greater than the half of the size of the array size.
#
# Input : {3, 3, 4, 2, 4, 4, 2, 4}
# Output : No Majority Element

def majority_elements(nums):
    sums = {}

    for n in nums:
        if n not in sums:
            sums[n] = 1
        else:
            sums[n] += 1

        if sums[n] > len(nums)/2:
            return n


numbers = 3, 3, 4, 2, 4, 4, 2, 4, 4
print(majority_elements(numbers))