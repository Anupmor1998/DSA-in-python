arr = [int(i) for i in input().split()]
def minJumps(arr, n):
      if (n <= 1):
        return 0
     
      if (arr[0] == 0):
        return -1
    
      maxReach = arr[0]  
      step = arr[0]
      stepcounter = arr[0]
      jump = 1 
     
      for i in range(1, n):
     
        if (stepcounter >= n-1):
          return jump
     
        maxReach = max(maxReach, i + arr[i])
     
        step -= 1
     
        if (step == 0):
          jump += 1
          if(i >= maxReach):
            return -1
          step = maxReach - i
          stepcounter += step
      return -1