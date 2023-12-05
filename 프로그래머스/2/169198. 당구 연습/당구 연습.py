def solution(m, n, startX, startY, balls):
    answer = []
    hall = [[0] * m for _ in range(n)]
    for i in balls:
        x = startX
        y = startY
        nx = i[0]
        ny = i[1]
        k = []
        
        if x != nx or y < ny:
            y1 = -y
            distance = (x-nx)**2 + (y1-ny)**2
            k.append(distance)
        if x != nx or y > ny:
            y1 = n*2 - y
            distance = (x-nx)**2 + (y1-ny)**2
            k.append(distance)
        if y != ny or x < nx:
            x1 = -x
            distance = (x1-nx)**2 + (y-ny)**2
            k.append(distance)
        if y != ny or x > nx:
            x1 = m*2 - x
            distance = (x1-nx)**2 + (y-ny)**2
            k.append(distance)
            
        answer.append(min(k))
    return answer