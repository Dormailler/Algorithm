def solution(ineq, eq, n, m):
    a = ""
    if ineq == "<":
        if eq == "=":
            a = n <= m
        else:
            a = n < m
    else:
        if eq == "=":
            a = n >= m
        else:
             a = n > m

    return int(a)
