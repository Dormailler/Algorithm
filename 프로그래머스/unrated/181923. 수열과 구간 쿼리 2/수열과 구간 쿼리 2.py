def solution(arr, queries):
    answer = []
    for s,e,k in queries:
        num = 10e8
        for i in range(s,e+1):
            if arr[i] > k:
                if arr[i] < num:
                    num = arr[i]
        if num == 10e8:
            answer.append(-1)
        else:
            answer.append(num)
    return answer