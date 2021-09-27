# Given an integer array nums,
# move all 0's to the end of it while
# maintaining the relative
# order of the non-zero elements.
#
# Note that you must do this in-place
# without making a copy of the array.

def moveZeroes(nums):
    for num in nums:
        if num == 0:
            nums.remove(num)
            nums.extend([0])
            print(nums)
    return nums

result = moveZeroes([0,1,0,3,12])

print(result)