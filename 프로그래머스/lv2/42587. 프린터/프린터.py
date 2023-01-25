def solution(priorities, location):
    p = list(priorities)
    answer = 0
    while 1:
        if p[0] != max(p):
            p.append(p.pop(0))
            if location == 0:
                location += len(p)
            location -= 1
        else:
            p.pop(0)
            answer += 1
            if location == 0:
                break
            location -= 1
    return answer
print(solution([2,1,3,2],2))