def solution(board):
    n = len(board)
    m = len(board[0])
    dp = [[0 for j in range(m)] for i in range(n)]
    ans = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                dp[i][j] = 0
            else:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
            ans = max(ans, dp[i][j])
    return ans**2