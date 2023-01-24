a = list(map(int,input().split()))
st = [0,0,0]
b = a
num = 0
def count():
    num = 0
    st[0] +=1
    if st[0] == 16:
        st[0] = 1
    st[1] +=1
    if st[1] == 29:
        st[1] = 1
    st[2] +=1
    if st[2] == 20:
        st[2] = 1
    num+=1
    return num
while a[0] != st[0] or a[1] != st[1] or a[2] != st[2] :
    num += count()
print(num)