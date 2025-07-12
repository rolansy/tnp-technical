nl=int(input())
stack=[]
reg=0
i=0
inps=[]
for _ in range(nl):
    inps.append(list(map(str,input().strip().split())))
while i<nl:
    l=inps[i]
    i+=1 
    if l[0]=='PUSH':
        stack.insert(0,int(l[1]))
    elif l[0]=='STORE':
        reg=stack.pop(0)
    elif l[0]=='LOAD':
        stack.insert(0,reg)
    elif l[0]=='PLUS':
        m=stack.pop(0)
        n=stack.pop(0)
        stack.insert(0,m+n)
    elif l[0]=='TIMES':
        m=stack.pop(0)
        n=stack.pop(0)
        stack.insert(0,m*n)
    elif l[0]=='IFZERO':
        if stack.pop(0)==0:
            i=int(l[1])
    elif l[0]=='DONE':
        break
print(stack[0])
        