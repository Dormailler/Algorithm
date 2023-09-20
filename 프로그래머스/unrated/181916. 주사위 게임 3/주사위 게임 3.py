def solution(a, b, c, d):
    dic = {}
    dic[a] = 1
    if b not in dic:
        dic[b] = 1
    else:
        dic[b] += 1
    if c not in dic:
        dic[c] = 1
    else:
        dic[c] += 1
    if d not in dic:
        dic[d] = 1
    else:
        dic[d] += 1
    point = 0
    if len(dic) == 1:
        point += a * 1111
    elif len(dic) == 2:
        a = []
        b = []
        for i in dic:
            if dic[i] == 1:
                a.append(i)
            elif dic[i] == 2:
                b.append(i)
            else:
                a.insert(0,i)
        if len(b) == 2:
            point += (b[0] + b[1]) * abs(b[0]-b[1])
        else:
            point += (10*a[0] + a[1]) ** 2
    elif len(dic) == 3:
        a = []
        for i in dic:
            if dic[i] != 2:
                a.append(i)
        point += a[0] * a[1]
    else:
        point += min(a,b,c,d)
        
        
        
    return point