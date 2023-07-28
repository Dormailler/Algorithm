import re

def solution(myString, pat):
    li = re.findall(rf'\w*{pat}', myString)
    
    return li[0]