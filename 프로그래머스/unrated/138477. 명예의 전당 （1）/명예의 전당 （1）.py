def solution(k, score):
    award = []
    answer = []
    for i in score:
        if len(award) < k:
            award.append(i)
            award = sorted(award,reverse=True)
        else:
            award = sorted(award,reverse=True)
            if award[-1] < i:
                award[-1] = i
            award = sorted(award,reverse=True)
        answer.append(award[-1])
    return answer