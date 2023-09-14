def solution(rank, attendance):
    r_rank = []
    i = 1
    while len(r_rank) < 3:
        num = rank.index(i)
        if attendance[num] == True:
            r_rank.append(num)
        i += 1
    a = r_rank[0]
    b = r_rank[1]
    c = r_rank[2]
    return a * 10000 + b * 100 + c