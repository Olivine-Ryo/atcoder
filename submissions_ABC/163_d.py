n,k=[int(i) for i in input().split()]
s=0
#g=n*(n+1)//2
lim=10**9+7
ma=n*(n+1)//2
mi=n*(n+1)//2
for i in range(n+2-k):
    #print(mi,ma)
    s = (s+ma-mi+1)%lim
    ma -= i
    mi -= (n-i)
    #print(ma-mi+1)
print(s%lim)
