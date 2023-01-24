n = int(input())
stack = []
for i in range(1,1000):
    stack.append(i**2)
dp = [0] *(n+1)
num = 0
for i in range(1,n+1):
    s= []
    for j in stack:
        if j > i:
            break
        s.append(dp[i-j])
    dp[i] = min(s)+1
print(dp[n])