def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        i = list(i)
        ni = -1
        n = 0
        pi = 100
        for j in range(len(skill)):
            if skill[j] not in i:
                pi = j
                continue
            else:
                if j > pi:
                    n = 1
                    break
                if ni < i.index(skill[j]):
                    ni = i.index(skill[j])
                else:
                    n = 1
                    break
        if n == 0:
            answer+=1
    return answer