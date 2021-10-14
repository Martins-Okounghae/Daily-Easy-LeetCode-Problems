def mostCommon(nums):
    count ={}
    for num in nums:
        key = count.keys()
        if num not in key:
            count[num] = 1
        else:
            count[num] += 1
    return max(count,key=count.get)

result = mostCommon([1,2,3,5,8,8,8,8,8,8,6])

print(result)