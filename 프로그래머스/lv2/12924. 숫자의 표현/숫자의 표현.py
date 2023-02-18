def solution(n):
    answer = 1
    for i in range(1,n//2+1):
        a = i
        temp = 1
        while a < n:
            a += i+temp
            temp += 1
        if a == n:
            answer +=1
    return answer