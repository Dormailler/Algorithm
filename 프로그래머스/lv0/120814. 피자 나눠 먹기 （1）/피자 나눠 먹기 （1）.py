def solution(n):
    answer = 1
    a = n
    while a > 7:
        answer += 1
        a -= 7
    return answer