def trappingWater(arr, n):

    water = 0
    left_max = 0
    right_max = 0

    lo = 0
    hi = n-1

    while lo <= hi:
        if arr[lo] < arr[hi]:
            if arr[lo] > left_max:
                left_max = arr[lo]
            else:
                water += left_max - arr[lo]
            lo += 1
        else:
            if arr[hi] > right_max:
                right_max = arr[hi]
            else:
                water += right_max-arr[hi]
            hi -= 1
    return water


print(trappingWater([7, 4, 0, 9], 4))
