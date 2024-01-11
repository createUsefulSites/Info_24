# import random
#
#
# def createRandomValue():
#     randomLength = random.randint(5, 9)
#     resultString = ''
#     for i in range(randomLength):
#         resultString += chr(random.randint(65, 90))
#     return resultString
#
#
# file = open("24_2.txt", "w")
# k = 0
# while k < 1000:
#     file.write(createRandomValue() + ' ' + createRandomValue())
#     k += 1
#     if k < 1000:
#         file.write('\n')
# file.close()


file = open("24_2.txt")
pairs = []
vowels = 'AEIOUY'
consonants = 'BCDFGHJKLMNPQRSTVWXYZ'
mx_sum = 0
answer = ''
for element in file:
    sm_symbols = 0
    (a, b) = element.replace('\n', '').split(' ')
    for i in range(len(a)):
        if a[i] in vowels:
            sm_symbols += 1
    for i in range(len(b)):
        if b[i] in consonants:
            sm_symbols += 1
    if mx_sum < sm_symbols:
        answer = a + b
        mx_sum = sm_symbols

print(answer)





