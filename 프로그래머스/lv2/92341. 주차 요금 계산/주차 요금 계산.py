from math import ceil
def solution(fees, records):
    n = fees[0] #기본시간
    nf = fees[1] #기본요금
    nt = fees[2] #단위시간
    tf = fees[3] #단위요금
    records.sort(key= lambda x:x.split()[1])
    dic = {}
    stack = []
    cdic = {}
    for i in records:
        i = i.split()
        if i[1] not in dic:
            dic[i[1]] = 0
        if i[2] == 'IN':
            dic[i[1]] -= int(i[0][0:2]) * 60 + int(i[0][3:5])
            cdic[i[1]] = 1
        else:
            dic[i[1]] += int(i[0][0:2]) * 60 + int(i[0][3:5])
            cdic[i[1]] = 0
    for i in cdic:
        if cdic[i] == 1:
            dic[i] += 23*60+59
    d = sorted(dic.items())
    for i in d:
        if i[1] <= n:
            stack.append(nf)
        else:
            stack.append(nf + ceil((i[1]-n)/nt)*tf)
    return stack