def solution(strings, n):

    for i in range(len(strings)-1):
        if(strings[i][n] > strings[i+1][n]):
            temp = strings[i+1][n]
            print(strings[i][n]) 
            print(temp)
            strings[i] = strings[i+1]
            print(strings[i]) 
            strings[i+1] = temp
        
    answer = strings    
        
    
    return answer

print(solution(["sun", "bed", "car"],1))