from itertools import combinations as c
def solution(orders, course):
    answer = []
    dic = {}
    stack = []
    for n in course:
        for i in orders:
            m = 0
            k = list(i)
            if n > len(k):
                continue
            a = c(k,n)
            for st in a:
                st = ''.join(sorted(st))
                if st not in dic:
                    dic[st] = 1
                else:
                    dic[st] += 1
        for i in dic:
            m = max(m,dic[i])
        for i in dic:
            if dic[i] == m and m>=2:
                answer.append(i)
        dic = {}
    return sorted(answer)