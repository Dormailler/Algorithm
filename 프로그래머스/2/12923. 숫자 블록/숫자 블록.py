def solution(begin, end):
    answer = [0] * (end-begin+1)
    for i in range(begin-1,end):
        if i == 0:
            continue
        n = 2
        a = 1
        while n < int((i+1)**0.5+1) :
            if (i+1) % n == 0:
                if (i+1)// n <= 10000000:
                    a = (i+1)//n
                    break
                else:
                    a = n
            n += 1
        answer[i-begin+1] = a

    return answer

