def solution(k, d):
    answer = 0
    a = [(i*k)**2 for i in range(d//k+1)]
    c = d ** 2
    for i in a:
        num = c - i
        answer += int(num**0.5) // k +1
        
    return answer