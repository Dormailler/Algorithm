import sys
input = sys.stdin.readline
a,b = map(int,input().split())
s = [list(map(int,input().split())) for i in range(a)]
def t_1(arr):
    m = 0
    for i in range(a):
        for j in range(b-3):
            n = 0
            for x in range(4):
                n += arr[i][j+x] 
            m = max(m,n)
    for i in range(a-3):
        for j in range(b):
            n = 0
            for x in range(4):
                n += arr[i+x][j] 
            m = max(m,n)
    return m
def t_s(arr):
    m = 0
    for i in range(a-1):
        for j in range(b-1):
            n = 0   
            for x in range(2):
                for y in range(2):
                    n += arr[i+x][j+y] 
            m = max(m,n)
    return m
def t_L(arr):
    m = 0
    for i in range(a-2): 
        for j in range(b-1):
            n = 0   
            for x in range(3):
                n += arr[i+x][j] 
            n += arr[i+2][j+1]
            m = max(m,n)
    for i in range(a-2):  
        for j in range(b-1):
            n = 0   
            for x in range(3):
                n += arr[i+x][j+1] 
            n += arr[i+2][j]
            m = max(m,n)
    for i in range(a-1): 
        for j in range(b-2):
            n = 0   
            for x in range(3):
                n += arr[i+1][j+x] 
            n += arr[i][j+2]
            m = max(m,n)
    for i in range(a-1):   
        for j in range(b-2):
            n = 0   
            for x in range(3):
                n += arr[i][j+x] 
            n += arr[i+1][j+2]
            m = max(m,n)
    for i in range(a-2):   
        for j in range(b-1):
            n = 0   
            for x in range(3):
                n += arr[i+x][j+1] 
            n += arr[i][j]
            m = max(m,n)
    for i in range(a-2):   
        for j in range(b-1):
            n = 0   
            for x in range(3):
                n += arr[i+x][j] 
            n += arr[i][j+1]
            m = max(m,n)
    for i in range(a-1):   
        for j in range(b-2):
            n = 0   
            for x in range(3):
                n += arr[i][j+x] 
            n += arr[i+1][j]
            m = max(m,n)
    for i in range(a-1):   
        for j in range(b-2):
            n = 0   
            for x in range(3):
                n += arr[i+1][j+x] 
            n += arr[i][j]
            m = max(m,n)
    return m
def t_S(arr):
    m = 0
    for i in range(a-2):
        for j in range(b-1):
            n = 0   
            for x in range(2):
                n += arr[i+x][j]
            for y in range(2): 
                n += arr[i+y+1][j+1]
            m = max(m,n)
    for i in range(a-2):
        for j in range(b-1):
            n = 0   
            for x in range(2):
                n += arr[i+x][j+1]
            for y in range(2): 
                n += arr[i+y+1][j]
            m = max(m,n)
    for i in range(a-1):
        for j in range(b-2):
            n = 0   
            for x in range(2):
                n += arr[i][j+x]
            for y in range(2): 
                n += arr[i+1][j+1+y]
            m = max(m,n)
    for i in range(a-1):
        for j in range(b-2):
            n = 0   
            for x in range(2):
                n += arr[i][j+1+x]
            for y in range(2): 
                n += arr[i+1][j+y]
            m = max(m,n)
    return m
def t_N(arr):
    m = 0
    for i in range(a-1):
        for j in range(b-2):
            n = 0   
            for x in range(3):
                n += arr[i][j+x]
            n += arr[i+1][j+1]
            m = max(m,n)
    for i in range(a-1):
        for j in range(b-2):
            n = 0   
            for x in range(3):
                n += arr[i+1][j+x]
            n += arr[i][j+1]
            m = max(m,n)
    for i in range(a-2):
        for j in range(b-1):
            n = 0   
            for x in range(3):
                n += arr[i+x][j]
            n += arr[i+1][j+1]
            m = max(m,n)
    for i in range(a-2):
        for j in range(b-1):
            n = 0   
            for x in range(3):
                n += arr[i+x][j+1]
            n += arr[i+1][j]
            m = max(m,n)
    return m
print(max(t_N(s),t_1(s),t_s(s),t_L(s),t_S(s)))