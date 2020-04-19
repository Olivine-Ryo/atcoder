n,m=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]
a = n-sum(a)
if a<0:
    print(-1)
else:
    print(a)