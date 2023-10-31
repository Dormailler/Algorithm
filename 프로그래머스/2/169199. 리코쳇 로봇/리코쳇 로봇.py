from collections import deque
def solution(board):
    answer = 0
    n = len(board)
    m = len(board[0])
    queue = deque()
    for i in range(n):
        for j in range(m):
            if board[i][j] == "R":
                start = (i,j)
            if board[i][j] == "G":
                goal = [i,j]
    g1,g2 = goal[0],goal[1]
    visit = [[0] * m for _ in range(n)]
    visit[start[0]][start[1]] = 1
    queue.append(start)
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    c = 0
    
    
    while queue:
        x,y = queue.popleft()
        if x == g1 and y == g2:
            return visit[g1][g2]-1
        for i in range(4):
            nx = x
            ny = y
            while True:
                nx += dx[i]
                ny += dy[i]
                if 0<=nx<n and 0<=ny<m and board[nx][ny]=='D':
                    nx -= dx[i]
                    ny -= dy[i]
                    break
                if nx<0 or nx>=n or ny<0 or ny>=m:
                    nx -= dx[i]
                    ny -= dy[i]
                    break
            if not visit[nx][ny]:
                visit[nx][ny] = visit[x][y] + 1
                queue.append((nx, ny))
    if visit[g1][g2] == 0:
        return -1