def solution(board, h, w):
    answer = 0
    n = len(board)
    m = len(board[0])
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    now = board[h][w]
    for k in range(4):
        nx = h + dx[k]
        ny = w + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if now == board[nx][ny]:
                answer += 1
    return answer