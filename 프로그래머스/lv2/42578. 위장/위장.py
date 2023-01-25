def solution(clothes):
    n = len(clothes)
    dic = {}
    for i in range(n):
        if clothes[i][1] not in dic:
            dic[clothes[i][1]] = 1
        else:
            dic[clothes[i][1]] += 1
    a = 0
    x = 1
    for i in dic:
        x *= (dic[i]+1)
    answer = x-1
    return answer