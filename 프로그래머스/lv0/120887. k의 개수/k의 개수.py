def solution(i, j, k):
    answer = 0
    for x in range(i,j+1):
        x = list(str(x))
        answer += x.count(str(k))
    return answer