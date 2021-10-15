#Reverse Words in a String III

def reverseWord(s):
    newlist = [sub_str[::-1] for sub_str in s.split()]
    return " ".join(newlist)


result = reverseWord("Let's take LeetCode contest")

print(result)