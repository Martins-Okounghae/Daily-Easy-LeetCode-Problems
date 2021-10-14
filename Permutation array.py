def buildArray(nums):
    return[nums[nums[i]] for i in range(len(nums))]


result = buildArray([2,6,5,1,3,2,4])

#newresult = [5,4,2,6,1,5,3]

print(result)

