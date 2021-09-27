# Given an integer array nums
# sorted in non-decreasing order,
# return an array of the squares
# of each number sorted in non-decreasing order.


def sortedSquares(nums):
    newValues = []
    for num in nums:
        newValues.append(num**2)
    return sorted(newValues)


result = sortedSquares([-7,-3,2,3,11])
print(result)


