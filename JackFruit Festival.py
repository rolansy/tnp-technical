a,b=map(int,input().strip().split())
l=list(map(int,input().strip().split()))
print(sum(sorted(l)[-1:-1-b:-1]))