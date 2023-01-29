def solution(before, after):
    a = list(after)
    for i in range(len(before)):
        if before[i] in a:
            a.remove(before[i])
    if a == []:
        return 1
    else:
        return 0