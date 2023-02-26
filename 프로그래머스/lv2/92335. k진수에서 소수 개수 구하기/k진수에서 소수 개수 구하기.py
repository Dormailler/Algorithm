def solution(n, k):
    answer = 0
    num = ""
    while n > 0:
        num = str(n%k) + num
        n = n // k
    num = num.split('0')
    for i in num:
        x = 0
        if i == "" or i == "1":
            continue
        a = int(i)
        for j in range(2,int(a**0.5)+1):
            if a % j == 0:
                x = 1
                break
        if x == 0:
            answer += 1
    print(num)
    return answer