def solution(board, k):
    answer = 0
    x = len(board)
    y = len(board[0]) 
    for i in range(x):
        for j in range(y):
            if i+j <= k:
                answer += board[i][j]
    return answer