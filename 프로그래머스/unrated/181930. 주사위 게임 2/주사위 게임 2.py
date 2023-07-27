def solution(a, b, c):
    if a == b and b == c:
        return (a+b+c) * (3 * a**2 ) *(3*a**3)
    elif a != b and b != c and a != c:
        return a+b+c
    else:
        return (a+b+c)*(a**2+b**2+c**2)