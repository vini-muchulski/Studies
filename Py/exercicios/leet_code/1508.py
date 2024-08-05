def rangeSum( nums, n, left, right):
    sub_somas = []
    MOD = 10**9 + 7
    
    for i in range(0,len(nums)):
        somatorio = 0
        for j in range(len(nums[i:])):
            somatorio = (somatorio + nums[i+j] ) % MOD
            sub_somas.append(somatorio)
     
    sub_somas.sort()
    somatorio = 0
    for i in range(left-1,right):
        somatorio = (somatorio + sub_somas[i]) % MOD
        
    #print(somatorio)
    return somatorio
    
    
rangeSum([1,2,3,4],4,1,10)