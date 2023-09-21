def solution(keymap, targets):
    dic = {}
    answer = []
    for s in keymap:
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = i+1
            else:
                if dic[s[i]] > i+1:
                    dic[s[i]] = i+1
    for s in targets:
        d = 0
        num = 0
        for c in s:
            if c in dic:
                num += dic[c]
            else:
                answer.append(-1)
                d = 1  
                break
        if d == 1:
            continue
        answer.append(num)
            
    return answer