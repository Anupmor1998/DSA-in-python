arr = [int(i) for i in input().split()]

#kadane's algo
def maxSubarraySum(arr):
    max_sum = max = 0
    
    for i in arr:
        
        max += i
        if(max_sum < max):
            max_sum = max
            
        if(max < 0):
            max = 0
        
    return max_sum
    
print(maxSubarraySum(arr))
