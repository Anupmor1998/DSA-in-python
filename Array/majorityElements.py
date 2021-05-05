
def majorityElement(nums, n):

    if n == 1:
        return nums

    times = n//3

    temp = []

    d = {}

    for i in nums:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

    for i in list(set(nums)):
        if d[i] > times:
            temp.append(i)
    return temp

# O(1) Space Complexity Approach


def majorityElementTwo(nums, n):

    count1 = count2 = 0
    candidate1 = 0
    candidate2 = 1

    for i in nums:
        if i == candidate1:
            count1 += 1
        elif i == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1 = i
            count1 = 1
        elif count2 == 0:
            candidate2 = i
            count2 = 1
        else:
            count1 -= 1
            count2 -= 1
    return [i for i in (candidate1, candidate2) if nums.count(i) > n//3]


print(majorityElementTwo([1, 2, 2, 1, 1], 5))
