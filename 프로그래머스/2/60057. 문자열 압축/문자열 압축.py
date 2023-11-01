from collections import Counter as c
def solution(s):
    count = c(s)
    m = 0
    for i in count:
        if count[i] > m:
            m = count[i]
    result = []
    if len(s) == 1:
        return 1
    for i in range(1, len(s)+1):
        b = ""
        cnt = 1
        tmp=s[:i]

        for j in range(i, len(s)+i, i):
            
            if tmp==s[j:i+j]:
                cnt+=1
            else:
                if cnt!=1:
                    b = b + str(cnt)+tmp
                else:
                    b = b + tmp
                    
                tmp=s[j:j+i]
                cnt = 1
        
        result.append(len(b))
                        
                
    return min(result)