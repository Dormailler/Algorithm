def solution(wallpaper):
    n = len(wallpaper)
    m = len(wallpaper[0])
    xmin = 10e5
    xmax = 0
    ymin = 10e5
    ymax = 0
    for i in range(n):
        for j in range(m):
            if wallpaper[i][j] == "#":
                if i < xmin:
                    xmin = i
                if i > xmax:
                    xmax = i
                if j < ymin:
                    ymin = j
                if j > ymax:
                    ymax = j
    
    return [xmin,ymin,xmax+1,ymax+1]