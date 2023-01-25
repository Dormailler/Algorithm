def solution(citations):
    answer = 0
    for i in range(len(citations)):
        num1 = i+1
        num2 = 0
        for j in range(len(citations)):
            if citations[j] >= num1:
                num2+=1
        if num1 <= num2:
            answer = num1
    return answer
