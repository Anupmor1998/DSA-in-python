# Sort an array of 0s, 1s and 2s

arr = [int(i) for i in input().split()]


def sort012(arr, n):
    i = 0
    j = 0
    l = n-1

    while j <= l:
        if arr[j] == 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
        elif arr[j] == 1:
            j += 1
        else:
            arr[j], arr[l] = arr[l], arr[j]
            l-+1
    return arr


def sort012Two(arr, n):
    c1 = 0
    c2 = 0
    c3 = 0

    for i in range(n):
        if arr[i] == 0:
            c1 += 1
        elif arr[i] == 1:
            c2 += 1
        else:
            c3 += 1

    i = 0

    while(c1 > 0):
        arr[i] = 0
        i += 1
        c1 -= 1
    while(c2 > 0):
        arr[i] = 1
        i += 1
        c2 -= 1
    while(c3 > 0):
        arr[i] = 2
        i += 1
        c3 -= 1
    return arr


print(sort012Two(arr, len(arr)))
