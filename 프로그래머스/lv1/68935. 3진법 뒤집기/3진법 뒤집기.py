def solution(n):
    s = ''
    while n:
        s += str(n%3)
        n //= 3
    a = 1
    answer = 0
    for i in range(len(s)-1,-1,-1):
        answer += int(s[i]) * a
        a *= 3
    return answer