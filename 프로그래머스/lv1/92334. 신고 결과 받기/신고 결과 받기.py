def solution(id_list, report, k):
    dic = {}
    sdic = {}
    ndic = {}
    answer = []
    for i in id_list:
        dic[i] = ""
        ndic[i] = 0
        sdic[i] = 0
    for i in report:
        a,b = i.split()
        if b not in dic[a].split():
            dic[a] += b +" "
            ndic[b] += 1
    for i in ndic:
        if ndic[i] >= k:
            for j in dic:
                if i in dic[j].split():
                    sdic[j] += 1
    return [sdic[i] for i in sdic]