#Decompress Run-Length Encoded List

def decompressRLElist(nums):
    output = list()
    for i in range(0, len(nums), 2):
        subList = [nums[i + 1]] * (nums[i])
        print("The value of i", i)
        print("The value of (nums[i])", nums[i])
        print("The value of [nums[i + 1]]", [nums[i + 1]] *3)
        print("The value of nums[i + 1]" , nums[i + 1] * 3)
        output = output + subList
    return output


result = decompressRLElist([1,2,3,4])

print(result)