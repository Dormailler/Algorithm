import math
def solution(w,h):
    answer = 0
    g = math.gcd(w,h)
    return w*h - w - h + g
    