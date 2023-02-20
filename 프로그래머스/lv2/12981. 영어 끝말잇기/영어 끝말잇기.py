def solution(n, words):
    answer = []
    end = []
    order = 0
    num = 1
    for i in words:
        order += 1
        if end != []:
            if i[0] != end[-1] or i in answer:
                return [order,num]
            else:
                end.pop()
        end.append(i[-1])
        answer.append(i)
        if order == n:
            order = 0
            num += 1
    return [0,0]