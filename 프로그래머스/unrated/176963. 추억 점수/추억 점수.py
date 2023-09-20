def solution(name, yearning, photo):
    dic = {}
    result = []
    for n,s in zip(name,yearning):
        dic[n] = s
    for arr in photo:
        score = 0
        for i in arr:
            if i in dic:
                score += dic[i]
        result.append(score)
    return result