def solution(files):
    def findhead(x):
        end = 0
        n = 0
        for i in range(len(x)):
            if x[i].isdigit():
                end = i
                n = 1
                break
        if n == 0:
            end = len(x)
        return end
    def findint(x):
        s = ""
        n = 0
        for i in range(len(x)):
            if len(s) >=5 :
                break
            if x[i].isdigit():
                s += x[i]
                n = 1
            if n == 1 and x[i].isdigit() == False:
                break
        return int(s)
    return sorted(files,key = lambda x: (x[:findhead(x)].lower(),findint(x)))
    