n = int(input())
ans = n
for i in range(3,n+1):
    stack = []
    for j in range(2,int(i**0.5)+1):
        if j in stack:
            continue
        if i % j == 0:
            ans += 1
            stack.append(j)
            stack.append(i//j)
print(ans)