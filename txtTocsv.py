import sys, csv, os
class converter():
    def __init__(self):
        self.path = os.path.join('./emails')
        self.files = os.listdir(self.path)
        self.dictList = self.files[0].key()
        print(self.dictList)
        print("List of files : ", self.files)

    def toDic(filename):

        f = open(filename)

        lines = f.readlines()
        dic = {}
        f.close()

        for line in lines:
            line.rstrip('\n')
            temp = line.split(": ")
            if temp[0] == "\n":
                break
            dic[temp[0]] = temp[0:]
        with open('output.csv', 'w') as c:
            for key in dic.keys():
                c.write("%s,%s\n"%(key, dic[key]))

        return 0

if __name__ ==' __main__':
    converter.__init__()
    print("ok")