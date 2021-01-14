#!/usr/bin/env python3
from datetime import date
from datetime import timedelta


def addZeros(array):
    i = 0
    newArr = []
    for line in lines:
        if len(line) > i:
            i = len(line)
    for line in lines:
        while len(line) < i:
            line += '0'
        newArr.append(line)
    return newArr


def transpose(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]


def mapNumber(number):
    return {
        0: 0,
        1: 1,
        2: 8,
        3: 11,
        4: 21
    }[number]


f = open("input/input-ex")
lines = f.read().splitlines()
lines = addZeros(lines)
lines = transpose(lines)
today = date(2016, 1, 1)
wday = today.weekday()
nextSunday = today + timedelta(days=(6 - wday))
output = []
currentDate = nextSunday
for line in lines:
    for c in line:
        output.append((currentDate.strftime('%Y-%m-%d'), int(c)))
        currentDate = currentDate + timedelta(days=1)
outputFile = open("output/output-ex", "w")
print(output)
for line in output:
    toPrint = line[0] + " " + str(mapNumber(line[1]))
    print(toPrint)
    outputFile.write(toPrint + '\n')
