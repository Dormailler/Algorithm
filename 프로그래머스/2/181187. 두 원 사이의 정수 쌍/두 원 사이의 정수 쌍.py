from math import sqrt
def solution(r1, r2):
    answer = 0
    x1 = r1 ** 2
    x2 = r2 ** 2
    for i in range(1,r2):
        a = i ** 2
        y = int(sqrt(x2 - a))
        answer += y*4
    for i in range(1,r1):
        a = i ** 2
        y = sqrt(x1 - a)
        answer -= int(y) * 4
        if y % 1 == 0:
            answer += 4
        
    return answer + (r2-r1)*4 + 4