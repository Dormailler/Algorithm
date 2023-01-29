def solution(n):
    answer = 1
    a = 6
    while a%n != 0:
        a += 6
        answer += 1
    return answer