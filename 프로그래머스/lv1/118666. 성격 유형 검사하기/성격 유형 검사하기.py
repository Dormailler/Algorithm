def solution(survey, choices):
    dic = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    answer = ''
    for i in range(len(choices)):
        if choices[i] == 1:
            dic[survey[i][0]] += 3
        elif choices[i] == 2:
            dic[survey[i][0]] += 2
        elif choices[i] == 3:
            dic[survey[i][0]] += 1
        elif choices[i] == 5:
            dic[survey[i][1]] += 1
        elif choices[i] == 6:
            dic[survey[i][1]] += 2
        elif choices[i] == 7:
            dic[survey[i][1]] += 3
    if dic['R'] >= dic['T']:
        answer += 'R'
    else:
        answer += 'T'
    if dic['C'] >= dic['F']:
        answer += 'C'
    else:
        answer += 'F'
    if dic['J'] >= dic['M']:
        answer += 'J'
    else:
        answer += 'M'
    if dic['A'] >= dic['N']:
        answer += 'A'
    else:
        answer += 'N'
        
        
        
    return answer