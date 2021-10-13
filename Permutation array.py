def buildArray(nums):
    return ([nums[nums[i]] for i in range(len(nums))])



result = buildArray([1,2,3,5,7,10])