def solution(routes):
    answer = 0
    p = -40000
    routes.sort(key= lambda x:x[1])
    for start,end in routes:
        if p < start:
            answer += 1
            p = end
            
    return answer