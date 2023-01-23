n = int(input())
a = list(map(int, input().split()))
stack = []
dp = [0 for i in range(n)]
for i in range(n):
    for j in range(i):
        if a[i] > a[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
s = max(dp)
print(max(dp))
for i in range(len(dp)-1,-1,-1):
    if dp[i] == s:
        stack.append(a[i]) 
        s -= 1
    if s<0:
        break
for i in range(len(stack)-1,-1,-1):
    print(stack[i],end=' ')