def solution(s):
    num = 0
    trans = 0
    while s != "1":
        num += s.count('0')
        s = s.replace('0',"")
        s = bin(len(s))[2:]
        trans += 1
    return [trans,num]