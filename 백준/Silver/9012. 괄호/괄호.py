import sys
n = int(sys.stdin.readline())
stack = []
number = 0
for i in range(n):
    a = sys.stdin.readline()
    for i in range(len(a)):
        if a[i] == '(':
            number += 1
        elif a[i] == ')':
            number -= 1
        if number == -1:
            break
    if number == 0:
        print('YES')
    else:
        print('NO')
    number = 0