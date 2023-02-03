def solution(num, total):
    answer = []
    n = -100
    temp = -1
    j = 0
    while temp != total:
        temp = 0
        for i in range(n+j,n+j+num):
            temp += i
        j += 1
    for i in range(num):
        answer.append(n+j+i-1)
    return answer