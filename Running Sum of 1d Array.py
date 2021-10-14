#Running Sum of 1d Array

def runningSum(nums):

    for num in range(1,len(nums)):
        print(nums[num - 1])
        nums[num] += nums[num-1]

    return nums


result = runningSum([1,2,3,4])
print(result)