def solution(code):
    mode = 0
    answer = ""
    for i in range(len(code)):
        if mode == 0:
            if code[i] == "1":
                mode = 1
            else:
                if i % 2 == 0:
                    answer += code[i]
        else:
            if code[i] == "1":
                mode = 0
            else:
                if i % 2 == 1:
                    answer += code[i]
    if answer == "":
        return "EMPTY"
    return answer