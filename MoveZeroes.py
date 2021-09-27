# Given an integer array nums,
# move all 0's to the end of it while
# maintaining the relative
# order of the non-zero elements.
#
# Note that you must do this in-place
# without making a copy of the array.

# def moveZeroes(self , nums: List[int]) -> None:
#     if 0 in nums:
#         start = nums.index(0)
#         for i in range(start + 1 , len(nums)):
#             if nums[i] != 0:
#                 nums[start] , nums[i] = nums[i] , nums[start]
#                 start += 1






def moveZeroes(nums):
    for num in nums:
        if num == 0:
            nums.remove(num)
            nums.extend([0])
            print(nums)
    return nums

result = moveZeroes([0,1,0,3,12])

print(result)