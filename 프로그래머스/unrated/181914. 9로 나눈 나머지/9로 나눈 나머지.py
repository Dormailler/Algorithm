def solution(number):
    n = 0
    for i in range(len(number)):
        n += int(number[i])
    return n%9