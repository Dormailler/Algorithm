def solution(numbers):
    m = -10000000000
    for i in range(len(numbers)):
        for j in range(1,len(numbers)-i):
            m = max(m,numbers[i]*numbers[i+j])
    return m