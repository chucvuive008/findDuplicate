#find the first duplicate number in the array
a = [ 1, 2, 3, 4, 5, 9 ,8, 4,7]
def firstDuplicate(a):
    largest = max(a)
    ar = [0]*(largest+1)
    i = 0
    solution = 0
    while (i < len(a)):
        if ar[a[i]] == 0:
            ar[a[i]] = 1
            i = i+ 1
            solution = -1
        elif ar[a[i]] == 1:
            solution = a[i]
            break
    return solution

print (firstDuplicate(a))

#best solution
def firstDuplicate(a):
    mySet=set()
    for el in a:
        if el in mySet:
            return el
        mySet.add(el)
    return -1
