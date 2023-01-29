def solution(n):
    a = 1
    x = 0
    while a*x < n:
        x += 1
        a *= x 
    return x