def solution(targets):
    answer = 0
    targets.sort(key=lambda x :(x[0],x[1]))
    k1 = -1
    k2 = -1

    for i in targets:
        if i[0] > k2:
            k1 = i[0]
            k2 = i[1] - 1
            answer += 1
        else:
            k1 = max(k1,i[0])
            k2 = min(k2,i[1]-1)
    return answer