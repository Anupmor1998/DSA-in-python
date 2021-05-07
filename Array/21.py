# Subarray with 0 sum

def subArrayExists(arr, n):
    s = set()
    ans = 0
    for i in range(n):
        ans += arr[i]
        if ans == 0 or ans in s:
            return "Yes"
        s.add(ans)

    return "No"


print(subArrayExists([2, 4, -4, 0, 1], 5))
