import sys
a = sys.stdin.readline().rstrip()
m = 0
r = 0
out = 0
i = 0
while i<len(a):
    if a[i] == '(' and a[i+1] == ')':
        out += m
        i += 1      
    elif a[i] == '(':
        r = 0
        m += 1
        out +=1
    elif a[i] == ')':
        m -= 1
    i += 1
print(out)