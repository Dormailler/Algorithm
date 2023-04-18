n,k = map(int,input().split())
ans = 0
a = [0,0,0,0,0,0,0]
b = [0,0,0,0,0,0,0]
for i in range(n):
    s,y = map(int,input().split())
    if s == 0:
        a[y] += 1
    else:
        b[y] += 1
for i in a:
    ans += (i-1)//k+1
for i in b:
    ans += (i-1)//k+1  
print(ans) 