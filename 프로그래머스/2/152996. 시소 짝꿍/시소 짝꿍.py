from itertools import combinations as c
from collections import Counter
def solution(weights):
    answer = 0
    dic = Counter(weights)
    for i in dic:
        if dic[i] > 1:
            answer += dic[i] * (dic[i]-1) // 2

    s = set(weights)
    com = list(c(s,2))
    for i in com:
        a = [i[0]*2,i[0]*3,i[0]*4]
        b = [i[1]*2,i[1]*3,i[1]*4]
        for num in a:
            if num in b:
                answer += dic[i[0]] * dic[i[1]]
                break
    return answer