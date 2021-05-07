# Chocolate Distribution Problem

def findMinDiff(A, N, M):

    A.sort()
    start = 0
    end = N - 1
    mini = A[end] - A[start]

    for i in range(N - M + 1):
        mini = min(mini, A[i + M - 1] - A[i])

    return mini


print(findMinDiff([7, 3, 2, 4, 9, 12, 56], 7, 3))
