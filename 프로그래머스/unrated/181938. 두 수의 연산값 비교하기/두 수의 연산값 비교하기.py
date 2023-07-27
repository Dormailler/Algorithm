def solution(a, b):
    aob = int(str(a)+str(b))
    if aob > 2*a*b:
        return aob
    return 2*a*b