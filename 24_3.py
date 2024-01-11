# import random
#
#
# def createRandomValue():
#     return str(random.randint(48, 125)) + ' ' + str(random.randint(48, 125)) + ' ' + str(random.randint(48, 125))
#
#
# file = open("24_3.txt", "w")
# k = 0
# while k < 1000:
#     file.write(createRandomValue())
#     k += 1
#     if k < 1000:
#         file.write('\n')
# file.close()

file = open("24_3.txt")
answer = 0
for element in file:
    arr = element.replace('\n', '').split(' ')
    sm = 0
    for item in arr:
        if chr(int(item)).isdigit():
            sm += int(chr(int(item)))
    answer = max(answer, sm)

print(answer)
