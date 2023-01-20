import sys
s = list(sys.stdin.readline().rstrip())
stack = []
for i in range(len(s)):
    stack.append(''.join(s))
    s.pop(0)
stack = sorted(stack)
for i in stack:
    print(i)