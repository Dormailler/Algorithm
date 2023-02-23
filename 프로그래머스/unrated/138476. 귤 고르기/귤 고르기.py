def solution(k, tangerine):
    dic = dict()
    stack = []
    answer = 0
    for i in tangerine:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    for i in dic:
        stack.append(dic[i])
    stack.sort(reverse=True)
    for i in stack:
        k -= i
        answer += 1
        if k <= 0:
            return answer
    