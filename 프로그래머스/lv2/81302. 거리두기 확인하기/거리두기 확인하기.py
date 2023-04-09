def solution(places):
    answer = [1] * 5
    l = 0
    for x in places:
        for i in range(5):
            if answer[l] == 0:
                break
            for j in range(5):
                if x[i][j] == 'P':
                    if (j+1 < 5 and x[i][j+1] == 'P'
                       ) or (i+1 < 5 and x[i+1][j] == 'P'):
                        answer[l] = 0
                    if (j+2 < 5 and x[i][j+2] == 'P'):
                        if x[i][j+1] != 'X':
                            answer[l] = 0
                            
                    if (i+2 < 5 and x[i+2][j] == 'P'):
                        if x[i+1][j] != 'X':
                            answer[l] = 0
                    if (i+1 < 5 and j+1 < 5) and (x[i+1][j] != 'X' or
                                                 x[i][j+1] != 'X'
                                                 ) and x[i+1][j+1] == 'P':
                        answer[l] = 0
                    if (i != 0 and j+1 <5)  and (x[i-1][j] != 'X' or
                                                 x[i][j+1] != 'X'
                                                 ) and x[i-1][j+1] == 'P':
                        answer[l] = 0
        l += 1
    return answer