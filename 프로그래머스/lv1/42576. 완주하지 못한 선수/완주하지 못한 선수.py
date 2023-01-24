from collections import Counter
def solution(participant, completion):
    answer = ''
    p = Counter(participant)
    c = Counter(completion)
    a = p-c
    for i in a:
        answer = i
    return answer