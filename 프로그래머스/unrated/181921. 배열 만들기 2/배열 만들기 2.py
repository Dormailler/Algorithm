def solution(l, r):
    answer = []
    for i in range(l,r+1):
        a = 0
        if i % 5 != 0:
            continue
        for num in list(str(i)):
            if int(num) != 0 and int(num) != 5:
                a = 1
                break
        if a == 0:
            answer.append(i)
    if answer == []:
        return [-1]
    return answer