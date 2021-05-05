#Reverse the array

array = [int(i) for i in input().split()]
n = len(array)

def approach_one(arr,n):
    arr = array.copy()
    for i in range(n//2):
        arr[i],arr[n-i-1] = arr[n-i-1],arr[i]
    print(arr)

def approach_two(arr):

    arr1 = arr[::-1]
    print(arr1)
    
approach_one(array,n)
approach_two(array)
    

