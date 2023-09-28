def solution(n):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    visit = [[0 for _ in range(n)] for _ in range(n)]
    x = 0 
    y = 0
    num = 1
    direction = 1
    for i in range(n*n):
        answer[x][y] = num
        visit[x][y] = 1
        if direction == 1:
            if y + 1 < n and visit[x][y+1] == 0:
                y += 1
            else:
                direction = 2
        if direction == 2:
            if x + 1 < n and visit[x+1][y] == 0:
                x += 1
            else:
                direction = 3
        if direction == 3:
            if y - 1 >= 0 and visit[x][y-1] == 0:
                y -= 1
            else:
                direction = 4
        if direction == 4:
            if x - 1 >= 0 and visit[x-1][y] == 0:
                x -= 1
            else:
                direction = 1
                if y + 1 < n and visit[x][y+1] == 0:
                    y += 1
                else:
                    direction = 2
        
        num += 1
    return answer