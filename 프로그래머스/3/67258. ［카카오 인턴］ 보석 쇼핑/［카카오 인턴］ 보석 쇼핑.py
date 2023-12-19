from collections import Counter

def solution(gems):
    total = len(set(gems))  
    start, end = 0, 0
    answer = [0, len(gems) - 1]
    current = Counter()
    
    while end < len(gems):
        current[gems[end]] += 1 
        end += 1  
        while len(current) == total:
            if answer[1] - answer[0] > end - start - 1:
                answer = [start, end - 1]

            current[gems[start]] -= 1
            if current[gems[start]] == 0:
                del current[gems[start]]
            start += 1  

    return [answer[0] + 1, answer[1] + 1]
