def buildArray(nums):
    return ([nums[nums[i]] for i in range(len(nums))])



result = buildArray([1,2,3,5,4,0])

# Newresult = [2,3,5,0,4,1]

print(result)