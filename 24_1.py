# import random
#
#
# def randomSymbol():
#     return random.randint(0, 1)
#
#
# def createRandomValue(symbolType):
#     if symbolType == 0:
#         return chr(random.randint(65, 90))
#     return random.randint(0, 9)
#
#
# file = open("24_1.txt", "w")
# k = 0
# while k < 10000:
#     file.write(str(createRandomValue(randomSymbol())))
#     k += 1
# file.close()


max_int = [0, ""]
min_str = [10**10, ""]
one_ms = []
n = open("24_1.txt")
file = n.readline()

i = 0
while i < len(file):
    if file[i].isdigit():
        string_int = file[i]
        for j in range(i+1, len(file)):
            if file[j].isalpha() or j == len(file)-1:
                if max_int[0] <= len(string_int):
                    max_int[0] = len(string_int)
                    max_int[1] = string_int
                i = j-1
                break
            string_int += file[j]

    else:
        string_str = file[i]
        for j in range(i+1, len(file)):
            if file[j].isdigit() or j == len(file)-1:
                if min_str[0] >= len(string_str):
                    if len(string_str) == 1:
                        one_ms.append(string_str)
                    min_str[0] = len(string_str)
                    min_str[1] = string_str
                i = j-1
                break
            string_str += file[j]
    i += 1

if len(one_ms):
    print(sorted(one_ms)[-1] + max_int[1])
else:
    print(min_str[1] + max_int[1])



