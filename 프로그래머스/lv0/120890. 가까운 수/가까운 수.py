def solution(array, n):
    a = []
    m = 1000000
    answer = []
    for i in array:
        a.append(abs(i-n))
    for j in range(len(a)):
        if a[j] == min(a):
            answer.append(j)
    for k in answer:
        m = min(m,array[k])
    return m