def solution(msg):
    dic = {}
    stack = []
    num = 1
    for i in range(65,91):
        dic[chr(i)] = num
        num += 1
    i = 0 
    while i < len(msg):
        n = 1
        while msg[i:i+n] in dic:
            if i+n > len(msg):
                break
            n += 1
        if n > 1:
            stack.append(dic[msg[i:i+n-1]])
        else:
            stack.append(dic[msg[i]])
        if i+n != len(msg):
            dic[msg[i:i+n]] = num
        num += 1
        if n > 1:
            i += n-1
        else:
            i += 1
    return stack