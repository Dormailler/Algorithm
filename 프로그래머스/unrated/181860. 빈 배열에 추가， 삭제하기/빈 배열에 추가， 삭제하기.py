def solution(arr, flag):
    x = []
    for i in range(len(flag)):
        n = arr[i]
        if flag[i]:
            for i in range(arr[i]*2):
                x.append(n)
        else:
            for i in range(arr[i]):
                if x == []:
                    break
                x.pop()
    return x