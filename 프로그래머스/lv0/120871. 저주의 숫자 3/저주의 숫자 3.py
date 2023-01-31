def solution(n):
    num = [0]
    for i in range(0,200):
        if i%3 == 0:
            continue
        if '3' in list(str(i)):
            continue
        num.append(i)
    return num[n]
