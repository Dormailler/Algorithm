def solution(array):
    dic = dict()
    li = []
    for i in array:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 0
    for i in dic:
        if dic[i] == max(dic.values()):
            if li != []:
                return -1
            li.append(i)
    return li[0]