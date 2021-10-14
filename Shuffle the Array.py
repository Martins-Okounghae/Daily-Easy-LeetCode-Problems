#Shuffle the Array
import itertools
def shuffle_Array(nums, n):
    # new_Array = []
    #
    # for num in range(n):
    #     new_Array.append(nums[num::n])
    # return list(itertools.chain.from_iterable(new_Array))

    new_Array =[]

    for num in range(n):
        new_Array.append(nums[num])
        new_Array.append(nums[num+n])
    return new_Array


result = shuffle_Array([1,2,3,4,4,3,2,1], n = 4)

print(result)
