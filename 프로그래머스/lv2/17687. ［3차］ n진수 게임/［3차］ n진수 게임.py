def solution(n, t, m, p):
    s = '0'
    a = ['A','B','C','D','E','F']
    for i in range(1,t*m+1):
        c = ""
        while i > 0:
            if i%n >= 10 :
                c = a[i%n-10] + c 
            else:
                c = str(i%n) +c
            i //= n
        s += c
    return s[p-1:t*m:m]