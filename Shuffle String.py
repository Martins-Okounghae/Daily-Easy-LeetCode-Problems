#Suffle string

def restoreString( s, indices):
    ss = [''] * len(s)
    for i in range(len(s)):
        ss[indices[i]] = s[i]
        print(ss)

    return ''.join(ss)

result = restoreString("codeleet", indices = [4,5,6,7,0,2,1,3])


print(result)