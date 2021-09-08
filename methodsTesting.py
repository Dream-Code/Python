# Name: Steven Rivera
# Small Python programs testing methods

import random
from string import punctuation

def craps():
    'Craps game generating random values until win or lose is achieved'

    win = [7, 11]
    lose = [2, 3, 12]
    rollAgain = [1, 4, 5, 6, 8, 9, 10]

    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    score = dice1 + dice2

    print(dice1)
    print(dice2)
    #print('Score is: ', score)
   
    while score in rollAgain:
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        score = dice1 + dice2

        print(dice1)
        print(dice2)
        #print('Score is: ', score)
        

    if score in win:
        return 'You win!'
    elif score in lose:
        return 'You lose.'

def studentID():
    'Prompts for student name. If student not on record, allows user to add'
    student = {}
    
    while True:
        first = input('Enter the first name: ')
        last = input('Enter the last name: ')
        person = (last, first)
        
        if first == '':
            break
        
        elif person in student:
            ID = student[person]
            changeID = input('{} has ID {}. Update?: '.format(person, ID))

            if changeID == 'y':
                updateID = input('Student ID: ')
                student[person] = updateID
                
        else:
            ID = input('Student ID: ')
            student[person] = ID

    print()
    print('Contents of Dictionary:')
    for key in student:
       print ('%s has studentID %s' % (key, student[key]))
       


def wordIndex(letter):
    'Searches through a file for user-specified letter and outputs the line number for each word'

    
    letter = letter.upper()
    infile = open('TaleOfTwoCities.txt', 'r')
    lines = infile.readlines()              # List of lines
    infile.close()

   
    myDict = {}
    lineNum = 0
    
    for line in lines:
        lineNum += 1
        word = line.split()
        
        for item in word:
            item = item.upper()
            myDict[item] = lineNum
        #print(item)

        wordCount = 0
        dictCounter = {}   
        for item in myDict:
            if item[0] == letter:
                wordCount += 1
                dictCounter.update({item : lineNum})
            
    #print(myDict)
    #print(dictCounter)
    print()
    if wordCount == 0:
        print('There are no words that begine with "{}"'.format(letter))
    
    else:
        print('{:19} {:10} '.format('Word','Line Nbr'))
        for word, num in sorted(dictCounter.items()):
            print('{:10} {:10}'.format(word, dictCounter[word]))
        
        print()
        print('There are {} lines in the book'.format(str(lineNum)))
        print('There are {} words that begine with "{}"'.format(wordCount, letter))


def wordIndex2(fname, letter):

    d = {}                                      # Initialize dictionary
    lineNum = 0                                 # Initialize line counter
    p = punctuation.replace("'", "")            # 
    transTable = str.maketrans(p, ' ' * len(p))

    infile = open(fname, 'r')
    lines = infile.readlines()                  # List of strings
    infile.close()


    for line in lines:
        if line == '':                          # Check for EOF
            break
        lineNum += 1
        line = line.translate(transTable)       # Remove punctuation from each line
        wordList = line.split()

        for word in wordList:
            uWord = word.upper()                # Converts word to uppercase
            if uWord in d:                      # uWord is the dictionary key
                if lineNum in d[uWord]:
                    continue
                else:
                    d[uWord].append(lineNum)
            else:
                d[uWord] = []           # Dictionary value list
                d[uWord].append(lineNum)


    msg1 = '{:15} {:15}'
    print(msg1.format('Word', 'Line Nbr.'))

    wordCount = 0
    for(key, value) in sorted(d.items()):
        msg = '{:15} {}'
        if key[0] == letter.upper():
            wordCount += 1
            print(msg.format(key, str(value)[1: -1]))   # Convert to string and remove 1st and last char

    print('\nThere are', lineNum, 'lines in the book')


    if wordCount == 0:
        print('There are no words that begin with "', letter, '"')
    else:
        print('There are', wordCount, 'words that begin with "', letter, '"')


    return












    
    
