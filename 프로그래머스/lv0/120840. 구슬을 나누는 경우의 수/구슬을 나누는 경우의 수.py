def solution(balls, share):
    b = 1
    for i in range(1,balls+1):
        b *= i
    for j in range(1,share+1):
        b //= j
    for k in range(1,balls-share+1):
        b //= k
    return b