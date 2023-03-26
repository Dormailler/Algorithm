def rotate(arr,y1,x1,y2,x2):
    m = 10000
    arr2 = [[arr[i][j] for j in range(len(arr[0]))] for i in range(len(arr))]
    for i in range(x1,x2):
        arr2[y1][i+1] = arr[y1][i]
        arr2[y2][i] = arr[y2][i+1]
        m = min(m, arr[y1][i])
        m = min(m, arr[y2][i+1])
    for i in range(y1,y2):
        arr2[i+1][x2] = arr[i][x2]
        arr2[i][x1] = arr[i+1][x1]
        m = min(m, arr[i][x2])
        m = min(m, arr[i+1][x1])
    return arr2,m

        
def solution(rows, columns, queries):
    maxrows = 0
    for i in queries:
        maxrows = max(maxrows,i[2])
    init = [[i+j*columns+1 for i in range(columns) ]for j in range(maxrows)]
    answer = []
    for i in queries:
        init,k = rotate(init,i[0]-1,i[1]-1,i[2]-1,i[3]-1)
        answer.append(k)
    return answer