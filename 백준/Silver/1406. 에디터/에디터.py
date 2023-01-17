import sys
st = list(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline())
stack = []
cnt = len(st)
for i in range(n):
    a = sys.stdin.readline().split()
    if a[0] == 'L' and st :
            stack.append(st.pop())
    elif a[0] == 'D' and stack:
            st.append(stack.pop())
    elif a[0] == 'B' and st:
            st.pop()
    elif a[0] == 'P':
        st.append(a[1])
        cnt += 1
stack = "".join(st+list(reversed(stack)))
print(stack)
