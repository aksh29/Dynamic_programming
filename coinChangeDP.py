def getWays(S,n,lookup):
    temp=S
    m = len(temp)
    #base case
    if(n==0):
        return 1
    #Soln doent exist
    if(m<=0  and n>=1):
        return 0
    #Soln doent exist
    if(n<0):
        return 0

    key=(m,n)
    if(key not in lookup):
        lookup[key]=getWays(temp,n-temp[m-1],lookup) + getWays(temp[:m-1],n,lookup)
    
    return lookup[key]

arr = [1,2,3]
lookup={}
print(getWays(arr, 4,lookup))

#top down approach

