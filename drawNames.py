'''
Author: Will Roden
Date Last Modified: 12/3/17
Purpose - This program is designed to simulate drawing names for gifts (e.g. Christmas). It reads a file called
"poolOfNames.txt" and assigns a giftee to a giftor. This program is designed to not allow someone to buy for themselves,
their significant other, who they bought for last year, and anyone in the family they may be feuding with. In order for
this program to function properly, "poolOfNames.txt" must be set up in such a way that on each line of the text file,
the first name is the giftor and the second name is the person that giftor bought for last year, the third is their
significant other (if applicable) and fourth and beyond go to family feuds. This program also will re-write the read
file after it draws to set up for the drawing next year. It also writes a new file that contains the current run for
reference after the program is run
'''

from random import sample, shuffle
import datetime

class Person:
    def __init__(self, name, lastYear=None, sigOther=None,  famFeud=None):
        self.__name = name
        self.__lastYear = lastYear
        self.__sigOther = sigOther
        self.__famFeud = famFeud
        self.__thisYear = None

    def getName(self):
        return self.__name

    def setName(self, x):
        self.__name = x

    def getSigOther(self):
        return self.__sigOther

    def setSigOther(self, x):
        self.__sigOther = x

    def getFamFeud(self):
        return self.__famFeud

    def setFamFeud(self, x):
        self.__famFeud = x

    def getLastYear(self):
        return self.__lastYear

    def setThisYear(self, x):
        self.__thisYear = x

    def getThisYear(self):
        return self.__thisYear

    def isFamilyFeud(self):
        return self.__famFeud is not None

    def getFamilyFeudStr(self):
        result = ''
        if self.isFamilyFeud():
            for person in self.__famFeud:
                result += person + ' '
        return result

    def __str__(self):
        return self.getName()


def main():
    familyList = []
    now = datetime.datetime.now()
    in_file = open("poolOfNamesTest" + str(now.year) + ".txt", "r")  # open/read poolOfNames.txt and stores in in_file
    line = in_file.readline()  # read first line of names
    while line != "":  # keep running until there's nothing left in the document
        line = line.rstrip()  # pops of the new line character at the end of each line
        split = line.split()  # splits the two names on each line into a list
        if len(split) == 3:  # Same as above, but also adds significant other, if applicable
            for n in range(1, 3):
                if split[n] == 'None':  # 'None' means the person didn't play last year and/or has no significant other
                    split[n] = None
            familyList.append(Person(split[0], split[1], split[2]))
        else:  # Same as above, but also adds a family feud list
            feudList = []
            for i in range(3, len(split)):
                feudList.append(split[i])
            familyList.append(Person(split[0], split[1], split[2], feudList))
        line = in_file.readline()  # reads the next line from the document
    in_file.close()
    familyListShuffle = list(familyList)
    shuffle(familyListShuffle)  # shuffles the list for extra randomness
    badRun = True
    while badRun:  # keep running until we get a good run
        try:  # ValueError could be raised if nothing is left in the set after the person's 'cant buy for' people are removed
            currentNamePool = set()  # create/reset the set and add everyone's name if it has run this code multiple times
            for person in familyListShuffle:
                currentNamePool.add(person.getName())
            for person in familyListShuffle:
                temp = []  # temp list to store the names of people the current person cannot buy for
                if person.getName() in currentNamePool:
                    temp.append(person.getName())      # if the person's name in the current pool, add to temp
                if person.getLastYear() in currentNamePool:
                    temp.append(person.getLastYear())  # if the person they bought for last year is in the pool, add to temp
                if person.getSigOther in currentNamePool:
                    temp.append(person.getSigOther())  # add to temp significant others -- could be None type
                if person.isFamilyFeud():          # if there's a family feud, add to temp
                    for j in person.getFamFeud():
                        if j in currentNamePool:
                            temp.append(j)
                for takeOut in temp:  # if anyone in the temp list is in the current pool, take them out
                    if takeOut in currentNamePool:
                        currentNamePool.remove(takeOut)
                draw = sample(currentNamePool, 1)  # chooses who the person will be buying for this year
                person.setThisYear(draw[0])  # adds that attribute to the person instance
                currentNamePool.remove(person.getThisYear())  # removes the person drawn this round from the current pool
                for addBack in temp:  # adds the names in the temp list back to the current pool
                    if addBack is not None:
                        currentNamePool.add(addBack)
            badRun = False  # if it makes it this far, it was a good run
        except ValueError:  # if a ValueError is raised, we simply want to run the "try" code again until there's a good run
            badRun = True
    
    out_file = open("whoBuysForWhom" + str(now.year) + ".txt", "w")  # Produces a list to refer back to after the program runs
    for person in familyList:
        print(person.getName(), 'buys for', person.getThisYear())
        out_file.write(person.getName() + ' ' + 'buys for' + ' ' + person.getThisYear() + '\n')
    out_file.close()
    out_file = open("poolOfNames" + str(now.year + 1) + ".txt", "w")  # re-writes the .txt file it read from to set up for next year's drawing
    for person in familyList:
        out_file.write(person.getName() + ' ' + person.getThisYear())
        if person.getSigOther() is not None:
            out_file.write(' ' + person.getSigOther())
        else:
            out_file.write(' None')
        if person.isFamilyFeud():
            out_file.write(' ' + person.getFamilyFeudStr())
        out_file.write('\n')
    out_file.close()

		
if __name__ == '__main__':
	main()
