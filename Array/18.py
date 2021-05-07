# Count pairs with given sum

def getPairsCount(arr, k):
    # code here
    c = 0
    d = {}

    for i in arr:
        sub = k - i

        if sub in d:
            c += d[sub]
        d[i] = d.get(i, 0) + 1
    return c


print(getPairsCount([1, 5, 7, 1], 6))
