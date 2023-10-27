from functools import reduce

def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key=lambda x:[x[col-1],-x[0]])
    s_i = []
    for i in range(row_begin-1,row_end):
        s = 0
        for d in data[i]:
            s += d % (i+1)
        s_i.append(s)
    s_i = reduce(lambda x,y:x^y,s_i)
    return s_i