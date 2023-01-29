def solution(emergency):
    s = sorted(emergency,reverse=True)
    for i in range(len(emergency)):
        emergency[i] = s.index(emergency[i])+1
    return emergency