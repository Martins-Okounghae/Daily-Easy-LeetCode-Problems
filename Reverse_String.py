
def reverse_string(s):
    left = 0
    right = len(s)- 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left, right = left + 1, right - 1

print(reverse_string("Martins"))




