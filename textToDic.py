from splitmaking import toDic
import csv
import os

path = os.path.join('/home', 'bear', 'emails')
#os.chdir(path)
files = os.listdir(path)

print(files)

data_file = open('data.csv', 'w')
writer = csv.writer(data_file, delimiter=',')
for file in files:
    writer.writerow(toDic(file))
data_file.close()




