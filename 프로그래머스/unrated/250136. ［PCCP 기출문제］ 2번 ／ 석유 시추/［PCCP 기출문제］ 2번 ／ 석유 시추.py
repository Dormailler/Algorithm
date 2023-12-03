from collections import deque
def solution(land):
    answer = 0
    n = len(land)
    m = len(land[0])
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    k = [0] * m
    visited = [[0] * m for _ in range(n)]
    def bfs(a,b,visited,num):
        queue = deque()
        queue.append((a,b))
        visited[a][b] = 1
        num += 1
        p = []
        while queue:
            x,y = queue.popleft()
            if y not in p:
                p.append(y)
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and land[nx][ny] == 1: 
                    visited[nx][ny] = 1
                    num += 1
                    queue.append((nx,ny))
        for o in p:
            k[o] += num
        return num
    for j in range(m):
        for i in range(n):
            num = 0
            if land[i][j] == 1 and visited[i][j] == 0:
                num = bfs(i,j,visited,num)
    return max(k)