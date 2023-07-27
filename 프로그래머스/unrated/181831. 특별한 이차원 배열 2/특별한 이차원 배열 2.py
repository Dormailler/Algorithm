def solution(arr):
    a = 1
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if arr[i][j] != arr[j][i]:
                a = 0
                break
    return a