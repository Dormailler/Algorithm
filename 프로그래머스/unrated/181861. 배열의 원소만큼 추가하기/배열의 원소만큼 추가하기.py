def solution(arr):
    x = []
    for num in arr:
        for i in range(num):
            x.append(num)
    return x