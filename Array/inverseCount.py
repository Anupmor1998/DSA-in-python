def mergeSort(arr):
    inv_count = 0
    if(len(arr)>1):
        
        if(len(set(arr)) == 1):
            return 0
        
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        
        inv_count += mergeSort(left)
        inv_count += mergeSort(right)
        
        
        i = j = k = 0
        
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                inv_count += mid - i
                j += 1
            k += 1
        
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return inv_count
            
myList = [10,10,10]
print(mergeSort(myList))
# print(myList)
        
        
    
    