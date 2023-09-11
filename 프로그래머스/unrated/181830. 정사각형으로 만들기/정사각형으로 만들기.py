def solution(arr):
    answer = []
    x = 0
    if len(arr) > len(arr[0]):
        x = len(arr)
    else:
        x = len(arr[0])
    for i in range(x):
        temp = []
        for j in range(x):
            try:
                temp.append(arr[i][j])
            except:
                temp.append(0)
        answer.append(temp)
    return answer