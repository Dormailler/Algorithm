def solution(cards1, cards2, goal):
    ok = 0
    for i in goal:
        if cards1 != []:
            if i == cards1[0]:
                cards1.pop(0)
                ok += 1
                continue
        if cards2 != []:
            if i == cards2[0]:
                cards2.pop(0)
                ok += 1
    if ok == len(goal):
        return "Yes"
    else:
        return "No"