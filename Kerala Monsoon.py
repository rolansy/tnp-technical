n=int(input())
bldgs=[]
for _ in range(n):
    x,y=map(int,input().strip().split())
    bldgs.append((x,y))
bldgs.sort(reverse=True)
dp=[float('inf')]*n
dp[0]=1
for i in range(1,n):
    dp[i]=dp[i-1]+1
    
    for j in range(i):
        xi,yi=bldgs[i]
        xj,yj=bldgs[j]
        if abs(xi-xj)<=abs(yi-yj):
            dp[i]=min(dp[i],dp[j])
            
print(dp[n-1])