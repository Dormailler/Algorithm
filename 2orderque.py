def solution(operations):
    answer = []
    for i in operations:
        a = []
        if i == "D 1":
            if answer == []:
                continue
            answer.remove(max(answer))
        elif i == "D -1":
            if answer == []:
                continue
            answer.remove(min(answer))
        else:
            a = i.split(" ")
            answer.append(int(a[1]))
    if answer == []:
        answer = [0,0]
    else:
        answer = [max(answer),min(answer)]
    return answer
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))