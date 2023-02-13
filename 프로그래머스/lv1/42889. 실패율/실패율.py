import numpy as np
def solution(N, stages):
    st1 = [0] * (N+2)
    st2 = [0] * (N+2)
    st = [0] * N
    stack = []
    for i in stages:
        for j in range(1,i+1):
            st1[j] += 1
        st2[i] +=  1
    for i in range(1,len(st1)):
        if st1[i] == 0:
            continue
        st1[i] = st2[i] / st1[i] * 100
    for i,v in enumerate(st1[1:-1]):
        st1[i+1] = [i+1,st1[i+1]]
    st1 = st1[1:-1]
    st1 = sorted(st1,key = lambda x: x[1],reverse=True)
    for i in st1:
        stack.append(i[0])
    return stack
