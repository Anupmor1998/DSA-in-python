# Array Subset of another array

def isSubset(a1, a2):

    for i in a2:
        if i in a1:
            a1.remove(i)
        else:
            return "No"
    return "Yes"


print(isSubset([1, 3, 5, 7, 5, 8], [5, 8, 7]))
