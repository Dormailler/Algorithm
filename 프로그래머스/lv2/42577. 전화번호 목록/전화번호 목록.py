def solution(phone_book):
    n = len(phone_book)
    answer = True
    s = sorted(phone_book)
    stack = []
    for i in range(n-1):
        l = len(s[i])
        if s[i][0:l] == s[i+1][0:l]:
            answer = False
    return answer