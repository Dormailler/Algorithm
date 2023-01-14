n = int(input())
k = 0
c = 0
for i in range(n):
    c = 0
    a = list(input())
    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            continue
        else:
            for j in range(1,len(a)-i):
                if a[i] == a[i+j]:
                    c = 1
                    break
    if c == 0:
        k = k+1
print(k)