import textToDic as td
import os, sys, csv


path = os.path.join('./emails')
files = os.listdir(path)

print("List of files : ", files)

for file in files:
    td.toDic(file)
