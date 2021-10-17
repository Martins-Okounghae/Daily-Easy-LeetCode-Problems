#Sum of the Unique number

def sumofUniqueNumber(nums):

    dict = {}

    for num in nums:
        if num not in dict:
            dict[num] = num
        else:
            dict[num] = 0

    return sum(dict.values())




result = sumofUniqueNumber([1,3,2,3,2])

print(result)

