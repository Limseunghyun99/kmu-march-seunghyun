import sys

try:
    filename = sys.argv[1]
except:
    print("Please enter filename")

f = open(filename, 'r')
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

