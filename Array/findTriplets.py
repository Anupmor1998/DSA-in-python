def find3Numbers(A, n, X):
    A.sort()

    for i in range(n-2):
        low = i + 1
        high = n - 1

        while low < high:
            if A[i] + A[low] + A[high] == X:
                return "Yes"
            elif A[i] + A[low] + A[high] < X:
                low += 1
            else:
                high -= 1
    return "No"


print(find3Numbers([1, 4, 45, 6, 10, 8], 6, 13))
