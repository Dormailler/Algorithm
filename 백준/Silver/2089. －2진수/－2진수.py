a = int(input())
stack = []
if not a:
    print(0)
    exit()
while a:
    if a%-2:
        stack.append(1)
        a = a//-2+1
    else:
        stack.append(0)
        a = a//-2
for i in range(len(stack)-1,-1,-1):
    print(stack[i],end='')