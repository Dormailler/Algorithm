visited = [[0 for _ in range(101)] for _ in range(101)]
w = 0
for i in range(4):
    x1,y1,x2,y2 = map(int,input().split())
    for j in range(x1,x2):
        for k in range(y1,y2):
            if visited[j][k] == 0:
                w += 1
            visited[j][k] = 1
print(w)
