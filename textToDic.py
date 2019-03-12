import sys, csv, os, string
from datetime import datetime
import codecs

def toDic(filename):
    path = os.path.join('./emails', filename)
    f = open(path, 'r')

    lines = f.readlines()
    dic = {}
    f.close()

    for line in lines:
        line.rstrip('\n')
        temp = line.split(": ")
        if temp[0] == "\n":
            break
        elif temp[0] == "Date":
            core = temp[1].split(" ")
            chicken = ' '.join(core[1:-2])
            dic[temp[0]] = datetime.strptime(chicken, '%d %b %Y %H:%M:%S')
            print(dic)
        else:
            dic[temp[0]] = temp[1:]

    print("1st checkpoint")
    with open('output.csv', 'w') as data:
        for key in dic.keys():
            data.write("%s,%s\n" % (key, dic[key]))
            print(key, dic[key])
        data.close()

    return 0
