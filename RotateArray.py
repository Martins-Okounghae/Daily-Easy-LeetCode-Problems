# Given an array, rotate the array to
# the right by k steps,
# where k is non-negative.
# Do not return anything,
# modify nums in-place instead.

# def rotateArray(nums, val):
#     length = len(nums)
#     newArray = []
#     while length > 0:
#         newArray.append(nums[-val])
#         val -= 1
#         length -= 1
#
#     return newArray
#
#
# result = rotateArray([1,2,3,4,5,6,7,], 3)
#
# print(result)


def rotate(nums, k):
    length = len(nums)

    newArray = [0] * length

    for num in range(length):
        newArray[(num + k) % length] = nums[num]

    nums[:] = newArray

result = rotate([ 1, 2, 3, 4, 5, 6, 7],3 )

print(result)
