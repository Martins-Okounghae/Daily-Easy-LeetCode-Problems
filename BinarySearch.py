# Given an array of integers nums
# which is sorted in ascending order,
# and an integer target, write a function
# to search target in nums. If target exists,
# then return its index. Otherwise, return -1.
#
# You must write an algorithm with O(log n)
# runtime complexity.

def search(nums, target):
    first = 0
    last = len(nums) -1

    while first <= last:
        mid = first + (last - first) // 2

        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            last = mid - 1

        else:
            first = mid + 1
    return -1


result = search([-1,0,3,5,9,12],9)

print(result)