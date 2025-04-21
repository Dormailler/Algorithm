from itertools import combinations as c

def solution(n, q, ans):
    answer = 0
    l = list(range(1,n+1))
    arr = list(c(l,len(q[0])))
  
    for ar in arr:
        for i in range(len(q)):
            num = 0
            for val in q[i]:
                if val in ar:
                    num += 1
            if num != ans[i]:
                break
        else:
            answer += 1   
    return answer