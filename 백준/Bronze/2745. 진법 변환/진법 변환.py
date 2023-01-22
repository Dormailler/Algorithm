import  sys
a,b = sys.stdin.readline().split()
b = int(b)
stack = []
a = list(a)
s = 1
n = 0
stack = [0] * len(a)
if a[0] == 0:
    print(0)
    exit()
for i in range(len(a)-1,-1,-1):
    if a[i].isalpha() == 1:
        stack[i] = int(ord(a[i])-55)
    else:
        stack[i] = int(a[i])
    n += stack[i] * s
    s = s * b   
print(n)   
