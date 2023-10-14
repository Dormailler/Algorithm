def solution(storey):
    answer = 0
    s = list(str(storey))[::-1]
    for i in range(len(s)):
        num = int(s[i])
        if num < 5:
            answer += num  
        elif num == 5:
            answer += num 
            if i + 1 < len(s) and int(s[i+1]) > 4:
                s[i+1] = str(int(s[i+1])+1)
        else:
            answer += 10-num
            if i + 1 < len(s):
                s[i+1] = str(int(s[i+1])+1)
            else:
                answer += 1
    return answer