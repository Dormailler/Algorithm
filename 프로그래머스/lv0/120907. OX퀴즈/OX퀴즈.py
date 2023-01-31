def solution(quiz):
    result = []
    for i in quiz:
        li = i.split()
        if li[1] == "+":
            if int(li[4]) == int(li[0]) + int(li[2]):
                result.append('O')
            else:
                result.append('X')
        elif li[1] == '-':
            if int(li[4]) == int(li[0]) - int(li[2]):
                result.append('O')
            else:
                result.append('X')
    return result