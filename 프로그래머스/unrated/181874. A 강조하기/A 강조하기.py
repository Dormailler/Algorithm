def solution(myString):
    myString = myString.lower()
    while 'a' in myString:
        myString = myString.replace('a','A')
    return myString
        