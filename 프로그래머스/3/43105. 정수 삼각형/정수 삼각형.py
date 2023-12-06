from collections import deque
def solution(triangle):
    answer = []
    l = len(triangle)
    queue = deque()
    queue.append((triangle[0][0],[0,0]))
    while queue:
        num,idx = queue.popleft()
        m = 0
        x,y = idx
        nx = x + 1
        if nx >= l:
            answer.append(num)
            continue
        dy = [0,1]
        for i in dy:
            ny = y + i
            if ny < len(triangle[nx]):
                queue.append((num+triangle[nx][ny],[nx,ny]))
    return max(answer)