import math
q=int(input())
temp=q
while q>0:
    q-=1
    n,k=input().split()
    n,k=[int(n),int(k)]
    u,v=0,0
    a=[math.ceil(n/2)-1,n-math.ceil(n/2)]
    if k==1:
        print("Case #{}: {} {}".format(temp-q,a[0],n-a[0]-1))
    else:
        for i in range(2,k+1):
            x=max(a)
            del a[a.index(max(a))]
            u=math.ceil(x/2)-1
            v=x-math.ceil(x/2)
            a.append(u)
            a.append(v)
        print("Case #{}: {} {}".format(temp-q,max(u,v),min(u,v)))
        
