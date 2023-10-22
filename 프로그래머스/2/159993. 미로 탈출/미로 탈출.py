from collections import deque
def solution(maps):
    m = len(maps)
    n = len(maps[0])
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    e = 0
    queue = deque()
    visited = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if maps[i][j] == "S":
                queue.append([i,j,0])
                break
    l = bfs(maps,dx,dy,visited,m,n,queue,"L")
    if l == -1:
        return -1
    x = l[0]
    y = l[1]
    d = l[2]
    queue = deque([[x,y,0]])
    visited = [[0 for _ in range(n)] for _ in range(m)]
    e = bfs(maps,dx,dy,visited,m,n,queue,"E")
    if e == -1:
        return -1
    
    return d + e[2]

def bfs(maps,dx,dy,visited,m,n,queue,alpha):
    while queue:
        x,y,depth = queue.popleft()
        if maps[x][y] == alpha:
            return [x,y,depth]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and visited[nx][ny] == 0 and maps[nx][ny] != "X":
                visited[nx][ny] = 1
                queue.append([nx,ny,depth+1])
    return -1


        
        