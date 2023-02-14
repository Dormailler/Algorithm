def lotto(ans,cor):
    if cor == 6:
        ans.append(1)
    elif cor == 5:
        ans.append(2)
    elif cor == 4:
        ans.append(3)
    elif cor == 3:
        ans.append(4)
    elif cor == 2:
        ans.append(5)
    else:
        ans.append(6)
def solution(lottos, win_nums):
    max_correct = 0
    min_correct = 0
    answer = []
    for i in lottos:
        if i == 0 or i in win_nums:
            max_correct += 1
        if i in win_nums:
            min_correct +=1
    lotto(answer,max_correct)
    lotto(answer,min_correct)
    return answer