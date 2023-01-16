n,m = map(int,input().split())
a = []
b = [] 
result = []
for i in range(n):
    in1 = input().split()
    for i in range(m):
        a.append(in1[i])
for i in range(n):
    in2 = input().split()
    for i in range(m):
        b.append(in2[i])
for i in range(n):
    result = [int(a[j+m*i])+int(b[j+m*i]) for j in range(m)]
    for j in range(m):
        print(result[j],end=' ')
    if i == n-1:
        break
    print()