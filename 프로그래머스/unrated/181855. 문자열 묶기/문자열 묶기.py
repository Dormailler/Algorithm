def solution(strArr):
    dic = {}
    for i in strArr:
        if len(i) not in dic:
            dic[len(i)] = 1
        else: 
            dic[len(i)] += 1
    m = 0
    for i in dic:
        if dic[i] > m:
            m = dic[i]
    return m