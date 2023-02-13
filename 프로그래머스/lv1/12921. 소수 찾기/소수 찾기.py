def solution(n):
    answer = 0
    for i in range(2,n+1):
        a = 0
        for j in range(2,int(i**0.5) + 1):
            if i % j == 0:
                a = 1
                break
        if a == 0:
            answer += 1    
    return answer