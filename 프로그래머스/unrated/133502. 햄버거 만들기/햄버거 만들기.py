def solution(ingredient):
    a = 0
    answer = 0
    while a < len(ingredient)-2:
        if ingredient[a] == 1 and ingredient[a+1] == 2 and ingredient[a+2] == 3 and ingredient[a+3] == 1:
            answer += 1
            ingredient.pop(a)
            ingredient.pop(a)
            ingredient.pop(a)
            ingredient.pop(a)
            if a < 4:
                a = 0
            else:
                a -= 4
        else:
            a += 1
    return answer