def mergeOne(arr1, arr2, n, m): 
        # code here
        for i in range(n):
            if arr2[0] < arr1[i]:
                arr1[i],arr2[0] = arr2[0],arr1[i]
                arr2.sort()
                
        return arr1,arr2

#optimized approch
def mergeTwo(n1, n2, m,n): 
        # code here
        i = m-1
        j = 0
        while i>=0 and j<n:
            if n1[i]>n2[j]:
                n1[i],n2[j]=n2[j],n1[i]
            i-=1
            j+=1
        n1.sort()
        n2.sort()
        
print(mergeTwo([1,3,5,7],[0,2,6,8,9],4,5))