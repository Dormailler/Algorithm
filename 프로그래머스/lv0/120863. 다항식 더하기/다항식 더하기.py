def solution(polynomial):
    p = polynomial.split()
    n = 0
    num = 0
    answer = ''
    for i in p:
        if 'x' in list(i):
            if i[0].isdigit():
                n += int(i[:-1])
            else:
                n += 1
        elif i.isdigit():
            num += int(i)
    if n != 0 :
        if n == 1:
            answer = 'x'
        else:
            answer = str(n) + 'x'
        if num != 0:
            answer += ' + ' + str(num) 
    else:            
        answer = str(num)
    return answer