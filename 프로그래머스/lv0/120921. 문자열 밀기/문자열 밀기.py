def solution(A, B):
    A = list(A)
    B = list(B)
    n = 0
    for i in range(len(A)):
        if A == B :
            return n
        a = list(A)
        for i in range(1,len(A)):
            if i == len(A)-1:
                A[0] = a[i]
            A[i] = a[i-1]
        n += 1
    return -1