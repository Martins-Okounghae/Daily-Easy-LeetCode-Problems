# Given an integer array nums, return
# true if any value appears at least twice
# in the array, and return false if every
# element is distinct.

def contain_Duplicate(nums):

    SortedNums = sorted(nums)
    for num in range(len(SortedNums)-1):
        if SortedNums[num] == SortedNums[num + 1]:
            return True
    return False



result = contain_Duplicate([1,2,3])

print(result)

