def solution(data, ext, val_ext, sort_by):
    answer = []
    dic = {"code":0,"date":1,"maximum":2,"remain":3}
    i = dic[ext]
    s = dic[sort_by]
    for d in data:
        if d[i] < val_ext:
            answer.append(d)
    answer.sort(key=lambda x:x[s])
    return answer