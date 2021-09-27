# Given a 1-indexed array of integers
# numbers that is already sorted in non-decreasing
# order,
# find two numbers such that they add up to a
# specific target number. Let these two numbers
# be numbers[index1] and numbers[index2]
# where 1 <= first < second <= numbers.length.
#
# Return the indices of the two
# numbers, index1 and index2, as an integer array
# [index1, index2] of length 2.
#
# The tests are generated such that
# there is exactly one solution.
# You may not use the same element twice.


def twoSum2(numbers, target):
    count = {}
    for key, value in enumerate(numbers, 1):
        compliment = target - value

        if compliment in count:
            return count[compliment], key
        else:
            count[value] = key


result = twoSum2([2, 7, 11, 15], 9)
print(result)
