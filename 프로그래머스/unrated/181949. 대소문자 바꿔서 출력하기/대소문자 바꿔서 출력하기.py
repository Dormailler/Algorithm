str = input()
str_list = list(str)
result = []
for i in str_list:
    if i.isupper() == 1:
        result.append(i.lower())
    else:
        result.append(i.upper())
print(''.join(result))