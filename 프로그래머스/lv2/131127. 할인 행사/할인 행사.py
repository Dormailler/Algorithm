def solution(want, number, discount):
    dic = {}
    answer = 0
    for i in range(len(want)):
        dic[want[i]] = number[i]
    for i in range(len(discount)):
        s = discount[i:i+10]
        copydic = dic.copy()
        for i in s:
            if i not in copydic:
                continue
            else:
                copydic[i] -= 1
        if all(copydic[i] <= 0 for i in copydic):
            answer += 1
    return answer