def solution(n):
    s = 0
    if n % 2 == 1:
        for i in range(0,n+1):
            if i % 2 == 1:
                s += i
        return s
    else:
        for i in range(0,n+1):
            if i % 2 == 0:
                s += i**2
        return s