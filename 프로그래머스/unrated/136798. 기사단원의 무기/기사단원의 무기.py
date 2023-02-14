def solution(number, limit, power):
    answer = 0
    stack = [1] * (number+1)
    for i in range(2,number+1):
        for j in range(i,number+1,i):
            stack[j] += 1
    for i in stack[1:]:
        if i <= limit:
            answer += i
        else:
            answer += power
    return answer