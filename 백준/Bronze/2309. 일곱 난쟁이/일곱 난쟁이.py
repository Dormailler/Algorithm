st = []
for i in range(9):
    n = int(input())
    st.append(n)
st = sorted(st)
n = sum(st) - 100
s = 0
for i in range(8):
    for j in range(1,9-i):
        if st[i] + st[i+j] == n:
            st.pop(i)
            st.pop(i+j-1)
            s = 1
            break
    if s==1:
        break
for x in st:
    print(x)