from math import sqrt
def solution(r1, r2):
    answer = 0
    x1 = r1 ** 2
    x2 = r2 ** 2
    p = 0
    for i in range(-r2,1):
        a = i ** 2
        y = sqrt(x2 - a)
        print(y)
        for j in range(0,r2+1):
            if a + j**2 > x2:
                break
            if a + j**2 < x1: 
                continue
            if j == 0 or i == 0:
                p += 1
            answer += 1
    return answer*4 - (p*2)