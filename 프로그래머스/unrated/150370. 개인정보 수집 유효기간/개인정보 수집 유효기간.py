def solution(today, terms, privacies):
    dic = {}
    answer = []
    for i in terms:
        grade,num = i.split()
        dic[grade] = int(num)
    ny,nm,nd = map(int,today.split("."))
    for i in range(len(privacies)):
        day,term = privacies[i].split()
        add = dic[term]
        y,m,d = map(int,day.split("."))
        m = m + add
        while m > 12 :
            y = y + 1
            m -= 12
        if d - 1 == 0 :
            m -= 1
            d = 28
        else:
            d -= 1
        if ny > y or (ny == y and nm > m) or (ny == y and nm == m and nd > d):
            answer.append(i+1)
    return answer