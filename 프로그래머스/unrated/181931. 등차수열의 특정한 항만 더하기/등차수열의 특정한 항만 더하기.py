def solution(a, d, included):
    n = a
    answer = 0
    for i in range(len(included)):
        if included[i]:
            answer += n
        n += d
    return answer