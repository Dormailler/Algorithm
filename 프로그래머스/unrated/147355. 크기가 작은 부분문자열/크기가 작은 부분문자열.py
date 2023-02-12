def solution(t, p):
    lp = len(p)
    answer = 0
    for i in range(len(t)-lp+1):
        if int(t[i:i+lp]) <= int(p):
                   answer +=1
    return answer