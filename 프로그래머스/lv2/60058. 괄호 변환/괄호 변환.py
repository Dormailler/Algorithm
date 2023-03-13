def split(a):
        dic = {'(':0,')':0}
        st1 = ''
        st2 = ''
        for i in range(len(a)):
            st1 += a[i]
            dic[a[i]] += 1
            if dic['('] == dic[')']:
                st2 = a[i+1:]
                break
        return st1,st2

def perfect(a):
        i = 0
        n = 0
        a = list(a)
        p = len(a)
        while i < p-1:
            if a[i] == '(' and a[i+1] == ')':
                a.pop(i)
                a.pop(i)
                p = len(a)
                i -= 2
            i += 1
        if a == []:
            return True

def sol(p):
    if p == "":
        return ""
    u,v = split(p)
    t = perfect(u)
    if t:
        return u + sol(v)
    else:
        a = '(' + sol(v) +')'
        u = list(u)
        u.pop()
        u.pop(0)
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        return a +''.join(u)
def solution(p):
    return sol(p)