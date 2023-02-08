def solution(n):
    n = list(str(n))
    n = int(''.join(sorted(n,reverse = True)))
    return n