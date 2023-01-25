def solution(progresses, speeds):
    answer = []
    n = 0
    while n < len(progresses):
        num = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        if progresses[n] >= 100:
            for i in range(n,len(progresses)):
                if progresses[i] >=100:
                    n+=1
                    num+=1
                else:
                    break
        if num != 0:
            answer.append(num)
    return answer