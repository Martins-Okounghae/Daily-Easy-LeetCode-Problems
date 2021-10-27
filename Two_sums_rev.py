

def twoSumsSolutions(num, target):

    count = {}

    for key, value in enumerate(num):
        compliment = target - value
        if compliment not in count:
            count[value] = key
        else:
            return count[compliment], key


result = twoSumsSolutions([2,4,6,8,10], 16)

print(result)


