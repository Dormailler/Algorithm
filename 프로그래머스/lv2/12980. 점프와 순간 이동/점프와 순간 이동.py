def solution(n):
    ans = 0
    if n == 1:
        return 1
    while n != 1:
        while n % 2 == 0:
            n //= 2
        ans += 1
        if n != 1:
            n -= 1
    return ans