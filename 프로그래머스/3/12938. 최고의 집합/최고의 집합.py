def solution(n, s):
    answer = []
    if n > s:
        return [-1]
    answer = [s//n] * n
    p = s%n
    i = -1
    
    while p:
        answer[i] += 1
        i -= 1
        p -= 1
    return answer