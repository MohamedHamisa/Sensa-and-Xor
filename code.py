def sansaXor(arr):
    n = len(arr)
    out = 0
    if n%2==0:
        return 0
    for i in range(0,len(arr),2):
        out^=arr[i]
    return out
  
  

