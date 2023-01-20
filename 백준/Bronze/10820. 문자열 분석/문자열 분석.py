import sys
while 1:
    try:
        o1 = 0
        o2 = 0
        o3 = 0
        o4 = 0
        s = input()
        for a in s:
            for i in range(97,123):
                if a == chr(i):
                    o1 += 1
                    break
            for i in range(65,91):
                if a == chr(i):
                    o2 += 1
                    break
            if a.isnumeric():
                o3 += 1
                continue
            elif a == ' ':
                o4 += 1
                continue
        print(o1,o2,o3,o4)  
    except EOFError:
        break