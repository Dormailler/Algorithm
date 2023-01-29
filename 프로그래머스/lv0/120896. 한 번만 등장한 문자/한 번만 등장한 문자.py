def solution(s):
    a = list(s)
    li = []
    for i in a:
        if a.count(i) == 1:
            li.append(i)
    li.sort()    
    return ''.join(li)