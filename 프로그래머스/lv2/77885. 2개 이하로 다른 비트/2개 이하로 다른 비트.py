def findnum(x):
    s = str(bin(x)[2:])
    for i in range(len(s)-1,-1,-1):
        if s[i] == '0':
            return compare(s[i+1:]) + x
    return compare(s) + x
def compare(a):
    return 2**(len(a)-1)
def solution(numbers):
    stack = []
    for i in numbers:
        if i % 2 == 0:
            stack.append(i+1)
            continue
        stack.append(findnum(i))
    return stack