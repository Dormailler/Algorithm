def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    p = 0
    m = len(B)
    for i in A:
        for j in range(p,m):
            if i < B[j]:
                answer += 1
                p = j+1
                break
    return answer