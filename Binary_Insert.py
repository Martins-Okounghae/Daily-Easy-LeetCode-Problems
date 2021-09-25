# Given a sorted array of distinct
# integers and a target value,
# return the index if the target is found.
# If not, return the index where it would be
# if it were inserted in order.
#
# You must write an algorithm with O(log n)
# runtime complexity.

def binarySearchInsert(nums, target):
    first = 0
    last = len(nums)-1

    while first <= last:
        mid = (first + last) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return first


result = binarySearchInsert([1, 3, 5, 6], target = 2)

print(result)