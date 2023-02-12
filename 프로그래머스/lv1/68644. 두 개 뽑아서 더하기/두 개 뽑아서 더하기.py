from itertools import combinations as com
def solution(numbers):
    num = com(numbers,2)
    return sorted(set([sum(i) for i in num]))
    