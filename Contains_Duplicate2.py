def contain_Duplicate(nums):

    numsdict = {}

    for num in nums:
        if num in numsdict:
            return True
        else:
            numsdict[num] = 1
    return False

result = contain_Duplicate([1,2,3])
print(result)