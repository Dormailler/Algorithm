from bisect import bisect_left, bisect_right

def solution(info, query):
    answer = []
    people = []
    conditions = {}

    for i in info:
        person_info = i.split()
        score = int(person_info.pop())
        people.append(person_info)
        
        # 모든 조합에 대한 점수를 저장
        for k in range(16):
            key = []
            for j in range(4):
                if k & (1 << j):
                    key.append(person_info[j])
                else:
                    key.append("-")
            key = tuple(key)
            if key in conditions:
                conditions[key].append(score)
            else:
                conditions[key] = [score]
    
    # 각 조합에 대한 점수를 정렬
    for key in conditions:
        conditions[key].sort()

    for q in query:
        sub, end, nior, f, score = q.replace(" and ", " ").split()
        score = int(score)
        key = (sub, end, nior, f)
        
        if key in conditions:
            scores = conditions[key]
            # 이진 탐색을 사용하여 query의 점수 조건을 만족하는 사람 수 계산
            left_idx = bisect_left(scores, score)
            right_idx = bisect_right(scores, score)
            num = len(scores) - left_idx
            answer.append(num)
        else:
            answer.append(0)

    return answer