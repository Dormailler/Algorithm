def solution(letter):
    answer = ''
    mose = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    s = letter.split()
    for i in s:
        for j in range(len(mose)):
            if i == mose[j] :
                answer += chr(97+j)
    return answer