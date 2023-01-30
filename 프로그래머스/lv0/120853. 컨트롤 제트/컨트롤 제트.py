def solution(s):
    li = s.split()
    answer = 0
    for i in range(len(li)-1,-1,-1):
        if li[i] == 'Z':
            li[i-1] = 0
        else:
            answer += int(li[i])
        
    return answer