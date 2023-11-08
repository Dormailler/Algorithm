from itertools import combinations as c
def solution(relation):
    answer = 0
    k = []
    n = len(relation)
    m = len(relation[0])
    num = 1
    d = [i for i in range(m)]
    while num <= m:
        com = list(c(d,num))  
        for i in com:
            a = []
            for j in range(n):
                p = []
                for x in i:
                    p.append(relation[j][x])
                if p in a:
                    break
                else:
                    a.append(p)
            else:
                l = 1
                u = 0
                for l in range(1,len(i)):
                    ic = c(i,l)
                    for b in ic:
                        if b in k:
                            u = 1
                            break
                if u == 0:
                    k.append(i)
                    answer += 1
        num += 1
    return answer