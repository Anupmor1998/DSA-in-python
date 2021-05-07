# Merge Intervals

def nextPermutation(nums):
    n = len(nums)

    if(n <= 2):
        return nums.reverse()

    pointer = n - 2

    while pointer >= 0 and nums[pointer] >= nums[pointer + 1]:
        pointer -= 1

    if(pointer == -1):
        return nums.reverse()

    for i in range(n-1, pointer, -1):
        if nums[pointer] < nums[i]:
            nums[pointer], nums[i] = nums[i], nums[pointer]
            break

    nums[pointer + 1:] = reversed(nums[pointer+1:])


print(nextPermutation([1, 2, 3, 4]))
