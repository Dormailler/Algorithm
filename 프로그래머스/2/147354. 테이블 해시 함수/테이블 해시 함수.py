def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key=lambda x:[x[col-1],-x[0]])
    s_i = []
    for i in range(row_begin-1,row_end):
        s = 0
        for d in data[i]:
            s += d % (i+1)
        s_i.append(s)
    k = 0
    for i in range(len(s_i)-1):
        a = bin(s_i[i])[2:]
        b = bin(s_i[i+1])[2:]
        if len(a) > len(b):
            while len(a) != len(b):
                b = '0' + b
        else:
            while len(a) != len(b):
                a = '0' + a
        a,b = list(a),list(b)
        for j in range(len(a)):
            if a[j] != b[j]:
                a[j] = '1'
            else:
                a[j] = '0'
        s_i[i+1] = int('0b'+''.join(a),2)

    return s_i[-1]