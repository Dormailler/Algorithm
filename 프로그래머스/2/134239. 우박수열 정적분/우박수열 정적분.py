def solution(k, ranges):
    answer = []
    route = [k]
    area = []
    stop = []
    while k > 1:
        if k % 2 == 0:
            k /= 2
        else:
            k = k * 3 + 1 
        route.append(k)
    for i in range(len(route) - 1):
        area.append((route[i] + route[i+1])/2)
        
    for r in ranges:
        s = r[0]
        e = len(area) + r[1]
        if s > e:
            answer.append(-1.0)
        elif s == e:
            answer.append(0.0)
        else:
            answer.append(sum(area[s:e]))

    return answer