# Given an array of integers nums
# and an integer target, return indices
#  of the two numbers such that they add up to target.
#
# You may assume that each input would
# have exactly one solution, and you may
# not use the same element twice.
#
# You can return the answer in any order.


def twosums(nums_list, target):
    result = {}

    for key, value in enumerate(nums_list):
        compliment = target - value
        if compliment in result:
            return key, result[compliment]
        result[value] = key

result = twosums([2,3,4,6,8,10], 18)

print(list(result))
