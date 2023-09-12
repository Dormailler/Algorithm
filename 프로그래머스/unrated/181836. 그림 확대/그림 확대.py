def solution(picture, k):
    answer = []
    for i in picture:
        string = ""
        for s in i:
            for _ in range(k):
                string += s
        for _ in range(k):
            answer.append(string)
    return answer