def solution(score):
    s = list(map(sum,score))
    n = 1
    li = [0] * len(s)
    for i in range(len(s)):
        temp = s.count(max(s))-1
        for i in range(s.count(max(s))):
            li[s.index(max(s))] = n
            s[s.index(max(s))] = -1
        n += 1 + temp
        if n > len(s):
            break
    return li