a,b = list(map(int,input().split()))
dp = [[0]*(201) for i in range(201)]

dp[1][2] = 2
dp[1][3] = 3
dp[2][2] = 3
for i in range(201):
    dp[i][1] = 1
    dp[1][i] = i
    dp[0][i] = 1
for i in range(2,201):
    for j in range(2,201):
        dp[i][j] = dp[i-1][j]+dp[i][j-1]
print(dp[a][b]%1000000000)