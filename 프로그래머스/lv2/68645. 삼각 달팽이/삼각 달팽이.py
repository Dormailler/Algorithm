def solution(n):
    answer = []
    stack = [[0] * (i+1) for i in range(n)]
    num = n * (n+1) // 2
    j = 0
    k = 0
    t = 0
    for i in range(1,num+1):
        stack[j][k] = i
        if j < n-1 and stack[j+1][k] == 0 and t == 0:
            j += 1
            if j == n-1 or stack[j+1][k] != 0:
                t = 1
        elif k < len(stack[j])-1 and stack[j][k+1] == 0 and t == 1:
            k += 1
            if k == len(stack[j])-1 or stack[j][k+1] != 0:
                t = 2
        elif stack[j-1][k-1] == 0:
            j -= 1
            k -= 1
            if stack[j-1][k-1] != 0:
                t = 0
    for i in stack:
        for j in i:
            answer.append(j)
    return answer