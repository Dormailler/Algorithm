n1,n2 = map(int,input().split())
n = list(map(int,input().split()))
n = sorted(n)
for i in range(n1):
    if(i == n2-1):
        break
    n.pop()
print(n[-1])