def getWays(S,n):
    temp=S
    m = len(temp)
    #base case
    if(n==0):
        return 1
    #Soln doent exist
    if(m<=0  and n>=1):
        return 0
    if(n<0):
        return 0
    
    return getWays(temp,n-temp[m-1]) + getWays(temp[:m-1],n)

arr = [1,2,3]
print(getWays(arr, 4))