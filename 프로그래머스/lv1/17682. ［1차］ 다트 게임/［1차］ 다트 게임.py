def solution(dartResult):
    stack = []
    num = 0
    for i in range(len(dartResult)):
        if dartResult[i].isdigit() :
            if num != 0:
                stack.append(num)
            if dartResult[i+1] == '0':
                num = 0
                continue 
            if dartResult[i] == '0':
                if dartResult[i-1].isdigit():
                    num = 10
                else:
                    num = 0
            else:
                num = int(dartResult[i])
        else:
            if dartResult[i] == 'S':
                num *= 1
            elif dartResult[i] == 'D':
                num **= 2
            elif dartResult[i] == 'T':
                num **= 3
            elif dartResult[i] == '*':
                num *= 2
                if stack != []:
                    stack[-1] *= 2
            elif dartResult[i] == '#':
                num *= -1
    stack.append(num)
    print(stack)
    return sum(stack)