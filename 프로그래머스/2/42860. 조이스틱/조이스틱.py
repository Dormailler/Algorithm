def solution(name):
    s = 'A' * len(name)
    num = 0
    n = list(name)
    for i in n:
        o_num = ord(i)
        o = min(ord(i) - ord('A'),ord('Z') - ord(i) + 1)
        num += o

    l = len(name)
    a1 = 0
    p = 0
    answer = []
    for i in range(len(name)):
        if name[i] != "A":
            if p + l + a1 - i <= i - a1:
                p = p + l + a1 - i
                answer.append((l-i)*2 + a1)
                break

            answer.append(a1*2 + l-i)
            answer.append((l-i)*2 + a1)
            p = p + i - a1
            a1 = p
    if all(i == "A" for i in n):
        return num
    if answer == []:
        return num + p
    p = min(p,min(answer))
    p = min(p,l-1)
    return num + p
