#How many numbers are smaller than the current number

def smallerThanCurrent(nums):
    res =[]

    sortedArray = sorted(nums)

    for num in nums:
        res.append(sortedArray.index(num))
    return res



result = smallerThanCurrent([8,1,2,2,3])
print(result)