def solution(n):
    num = bin(n)[2:].count('1')
    for i in range(n+1,10000000):
        if bin(i)[2:].count('1') == num:
            return i