def solution(n):
    answer = 0
    if n == 1:
        return 1
    if n < 4:
        return 0
    
    def app(arr):
        k = len(arr)
        a = 0
        
        for i in range(n):
            c = [i for i in arr]
            if i in arr:
                continue
            for ind,v in enumerate(arr):
                if abs(k - ind) == abs(i - v):
                    break
            else:
                c.append(i)
                if len(c) == n:
                    return 1
                a += app(c)

        return a
    
    for i in range(n):
        a = [i]
        answer += app(a)
        
    
    return answer
