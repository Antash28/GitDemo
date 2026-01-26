# f = open('myfile.txt', 'r')

# while True:
#     line = f.readline()
#     print(line)
#     if not line:
#         print(line, type(line))
#         break
#     # print(line)


f = open('myfile.txt', 'r')

while True:
    line = f.readline()
    if not line:
        break
    print(line)
