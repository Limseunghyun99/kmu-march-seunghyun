
f = open('98429.txt', 'r')
lines = f.readlines()
dic = {}
f.close()


for line in lines:
    line.rstrip('\n')
    temp = []
    temp = line.split(": ")
    if temp[0] == "\n":
        break
    dic[temp[0]] = temp[1]


print(dic)
print(lines)

