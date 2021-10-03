# Given a string s,
# find the length of the longest
# substring without repeating characters.


def lengthoflongeststr(s):
    n = len(s)
    ans = 0

    # indexStore stores the current index of a character

    indexStore = {}

    i = 0

    # try to extend the range [i , j]

    for j in range(n):
        if s[j] in indexStore:
            i = max(indexStore[s[j]], i)

        ans = max(ans, j-i + 1)
        indexStore[s[j]] = j + 1
    return ans

result = lengthoflongeststr("abcabcbb")

print(result)
