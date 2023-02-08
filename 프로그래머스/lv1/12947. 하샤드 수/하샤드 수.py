def solution(x):
    li = list(str(x))
    d = 0
    for i in range(len(li)):
        d += int(li[i])
    return x % d == 0