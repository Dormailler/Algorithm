def solution(n):
    n = list(str(n))
    answer = [int(n[i]) for i in range(-1,-len(n)-1,-1)]
    return answer