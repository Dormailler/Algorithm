def solution(s):
    if (len(s) == 4 or len(s) == 6) and all([i.isdigit() for i in s]):
        return True
    return False