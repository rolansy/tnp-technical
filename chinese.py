n=int(input())
a=sorted(list(map(int,input().strip().split())))
b=sorted(list(map(int,input().strip().split())),reverse=True)
q=int(input())
c=0
for i in range(n):
    x=a[i]+b[i]
    if x>q:
        c+=(x-q)
print(c*100)