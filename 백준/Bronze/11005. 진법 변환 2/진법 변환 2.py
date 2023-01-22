import  sys
a,b = map(int,sys.stdin.readline().split())
stack = []
if a == 0:
    print(0)
    exit()
while a:
    stack.append(a%b)
    a //= b
for i in range(len(stack)-1,-1,-1):
    
    if stack[i] >= 10:
        stack[i] = chr(stack[i]+55)
    print(stack[i],end='')
