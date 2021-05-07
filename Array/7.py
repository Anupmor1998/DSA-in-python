# Cyclically rotate an array by one

arr = [1, 2, 3, 4]


def rotate(arr, n):
    arr1 = []

    arr1 = arr[-1:] + arr[:-1]

    return arr1


print(rotate(arr, len(arr)))
