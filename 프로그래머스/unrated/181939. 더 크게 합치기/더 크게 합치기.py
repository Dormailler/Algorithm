def solution(a, b):
    s_a = str(a)
    s_b = str(b)
    if s_a + s_b > s_b + s_a:
        return int(s_a + s_b)
    return int(s_b + s_a)