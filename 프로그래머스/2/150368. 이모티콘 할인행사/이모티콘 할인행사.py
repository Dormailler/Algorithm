from itertools import product as prod 
def solution(users, emoticons):
    answer = []
    users.sort(key=lambda x:x[0])
    
    p = [10,20,30,40]
    
    
    c = list(prod(p, repeat=len(emoticons)))
    
    for rep in c:
        if all(i < users[0][0] for i in rep):
            continue
        a = 0
        m = 0
        for dis,money in users:
            total = 0
            for i in range(len(rep)):
                if dis <= rep[i]:
                    total += emoticons[i] * (100-rep[i]) // 100
                if total >= money:
                    total = 0
                    a += 1
                    break
            m += total
        answer.append([a,m])
    answer.sort(key=lambda x:(x[0],x[1]),reverse=True)
    return answer[0]