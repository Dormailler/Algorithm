from itertools import combinations as p
def solution(dots):
    a = [0,1,2,3]
    li = list(p(a,2))
    answer = 0
    for i in range(len(li)//2):
        b = a.copy()
        c = []
        c.append(b.pop(li[i][0]))
        c.append(b.pop(li[i][1]-1))
        radb = (dots[b[0]][0] - dots[b[1]][0] ) / (dots[b[0]][1] - dots[b[1]][1])
        radc = (dots[c[0]][0] - dots[c[1]][0] ) / (dots[c[0]][1] - dots[c[1]][1])
        if radb == radc:
            return 1
    return answer