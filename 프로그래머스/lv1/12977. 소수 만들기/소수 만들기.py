from itertools import combinations as com
def solution(nums):
    c = com(nums,3)  
    answer = 0
    for i in c:
        a = 0
        for j in range(2,int(sum(i)**0.5)+1):
            if sum(i) % j == 0 :
                a = 1
                break
        if a == 0:
            answer += 1
    return answer