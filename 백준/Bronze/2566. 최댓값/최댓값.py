b = []
rmax = 0
ri = 0
for i in range(9):
    a = list(map(int,input().split()))
    b.append(a)
for i in range(9):
        bmax = max(b[i])
        if rmax < bmax:
            rmax = bmax
            ri = i
print(rmax)
print(ri+1, b[ri].index(rmax)+1)