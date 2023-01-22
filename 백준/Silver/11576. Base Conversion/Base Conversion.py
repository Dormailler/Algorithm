import  sys
a,b = map(int,sys.stdin.readline().split())
n = int(sys.stdin.readline())
s =  list(map(int,sys.stdin.readline().split()))
num = 0
stack = []
x = 1
for i in range(len(s)-1,-1,-1):
    num += s[i] * x
    x *= a
while num:
    stack.append(num%b)
    num //= b
for i in range(len(stack)-1,-1,-1):
    print(stack[i],end = ' ')