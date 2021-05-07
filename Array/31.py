def sb(a, n, x):
    # Smallest subarray with sum greater than x

    window_sum = 0
    start = 0
    min_len = n + 1

    for end in range(len(a)):
        window_sum += a[end]

        while window_sum > x:
            min_len = min(min_len, end - start + 1)
            window_sum -= a[start]
            start += 1

    if min_len == n + 1:
        return 0

    return min_len


print(sb([1, 4, 45, 6, 0, 19], 6, 51))
