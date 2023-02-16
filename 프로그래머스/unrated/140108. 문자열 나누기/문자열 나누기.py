def solution(s):
    s = list(s)
    x = s[0]
    x_num = 0
    notx_num = 0
    answer = 0
    a = 0
    for i in range(len(s)):
        if s[i] == x:
            x_num += 1
        else:
            notx_num += 1
        if x_num == notx_num:
            answer += 1
            if i == len(s)-1:
                break
            x = s[i+1]
            x_num = 0
            notx_num = 0
        if x_num != notx_num and i == len(s)-1:
            answer += 1
    return answer