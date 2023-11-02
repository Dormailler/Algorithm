def solution(park, routes):
    n = len(park)
    m = len(park[0])
    for i in range(n):
        for j in range(m):
            if park[i][j] == "S":
                x,y = i,j

    for i in routes:
        dircetion,num = i[0:1],int(i[2:])
        nx,ny = x,y
        a = 0
        if dircetion == "E":
            ny += num
        elif dircetion == "W":
            ny -= num
        elif dircetion == "S":
            nx += num
        else:
            nx -= num
        if 0 <= nx < n and 0 <= ny < m:
            c = 0
            mix = min(x,nx+1)
            mx = max(x,nx+1)
            miy = min(y,ny+1)
            my = max(y,ny+1)
            for dx in range(mix,mx):
                if park[dx][ny] == "X":
                    c = 1
                    break
            for dy in range(miy,my):
                if park[nx][dy] == "X":
                    c = 1
                    break
            if c == 0:
                x,y = nx,ny
    return [x,y]