def solution(num, k):
    n = list(str(num))
    if str(k) in n:
        return n.index(str(k))+1
    else:
        return -1