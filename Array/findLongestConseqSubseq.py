def findLongestConseqSubseq(arr, N):
    temp = 1
    maxi = 1
    arr.sort()
    arr = list(set(arr))
    i = 1
    while i < len(arr):
        if temp > maxi:
            maxi = temp
            if arr[i-1]+1 == arr[i]:
                temp += 1
            else:
                temp = 1
            i += 1
    if temp > maxi:
        maxi = temp
    return maxi


print(findLongestConseqSubseq([1, 4, 6, 2, 3, 8, 4], 7))
