def getWays(S,m,n):
    # m = len(temp)
    #base case
    if(n==0):
        return 1
    #Soln doent exist
    if(m<=0  and n>=1):
        return 0
    if(n<0):
        return 0
    
    return getWays(S,m,n-S[m-1]) + getWays(S,m-1,n)

arr = [1,2,3]
m= len(arr)
print(getWays(arr,m, 4)) 