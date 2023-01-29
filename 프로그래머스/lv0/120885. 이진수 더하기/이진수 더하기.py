def solution(bin1, bin2):
    n1 = 0
    n2 = 0
    x1 = 1
    x2 = 1
    for i in range(len(bin1)-1,-1,-1):
        if bin1[i] == '1':
            n1 += x1
        x1 *= 2
    for i in range(len(bin2)-1,-1,-1):
        if bin2[i] == '1':
            n2 += x2
        x2 *= 2
    answer = n1 + n2
    answer = bin(answer)[2:]
    return answer