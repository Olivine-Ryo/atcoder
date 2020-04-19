n=int(input())
a=[int(i) for i in input().split()]
ans=[0 for _ in range(n)]
for i in a:
    ans[i-1] += 1
for j in ans:
    print(j)