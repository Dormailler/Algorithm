def solution(numbers):
    li = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    num = ['0','1','2','3','4','5','6','7','8','9']
    for i in range(len(li)):
        numbers =  numbers.replace(li[i],num[i])
    return int(numbers)