from itertools import combinations as com
def solution(number):
    answer = 0
    li = com(number,3)
    for i in li:
        if sum(i) == 0:
            answer += 1
    return answer