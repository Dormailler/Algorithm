def solution(n, w, num):
    answer = 0
    x = 0 
    y = 0
    d = 0
    arr = [[0 for _ in range(w)] for _ in range(n//w+1)]
    for i in range(n):
        arr[y][x] = i+1
        if d == 0:
            x += 1
        else:
            x -= 1
        if x == w:
            x -= 1
            y += 1
            d = 1
        if x == -1:
            x = 0
            y += 1
            d = 0
    
    for i in range(len(arr)):
        for j in range(w):
            if arr[i][j] == num:
                for k in range(len(arr) - i):
                    if arr[i+k][j] != 0:
                        answer += 1
                break
    return answer