def solution(n):
    answer = []
    
    def hanoi(one, three, two, n): 
        if n == 1:
            answer.append([one, three])
        else:
            hanoi(one,two,three,n-1)
            hanoi(one,three,two,1)
            hanoi(two,three,one,n-1)
            
    hanoi(1,3,2,n)
    
    return answer