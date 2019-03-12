#import sys
#import csv
import os

def toDic(filename):

    f = open(filename, 'r')
    lines = f.readlines()
    dic = {}
    f.close()

    for line in lines:
        line.rstrip('\n')
        temp = line.split(": ")
        if temp[0] == "\n":
            break
        dic[temp[0]] = temp[0:]

    return dic
