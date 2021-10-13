# Sort the list based on how close the number is to 50

def myfunc(n):
    return abs(n-50)


thislist=[100, 60, 69, 85, 50]

thislist.sort(key=myfunc)

print(thislist)

