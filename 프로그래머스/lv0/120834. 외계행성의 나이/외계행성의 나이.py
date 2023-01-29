def solution(age):
    a = list(str(age))
    for i in range(len(a)):
        a[i] = chr(97+int(a[i]))
    return ''.join(a)