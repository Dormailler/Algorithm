def solution(n):
    r = ""
    num = ["4","1","2"]
    x = 3

    while n > 0:
        r = num[n%3] + r
        if n % 3 == 0:
            n -= 1
        n //= 3
    return r