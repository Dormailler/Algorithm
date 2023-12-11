from collections import deque
def solution(m, n, puddles):
    answer = 0
    maps = [[0] * m for _ in range(n)]
    dp = [[0] * m for _ in range(n)]
    for x,y in puddles:
        maps[y-1][x-1] = 1
    queue = deque()
    queue.append((1,0,1))
    queue.append((1,0,1))
    dx = [-1,0]
    dy = [0,-1]
    dp[0][0] = 1
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 1:
                continue
            if i-1 >= 0 and maps[i-1][j] == 0:
                dp[i][j] += dp[i-1][j]
            if j-1 >= 0 and maps[i][j-1] == 0:
                dp[i][j] += dp[i][j-1]
    return dp[i][j] % 1000000007