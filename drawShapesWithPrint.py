# Name: Steven Rivera
# Python program to draw shapes with the print function


def squareQuads(n):
    'draw n x n square with four quadrants of equal size'

    print('Quadrants')
    
    for row in range(n):                    # Outer row
        for col in range(n):                # Inner column - Creates a line everytime i in range(n)
            if row == 0 or row == n - 1:    # Prints first and last row full
                print('*', end = ' ')
            elif row == n // 2:             # Prints a full row at half n
                   print('*', end = ' ') 
            elif col == 0 or col == n - 1:  # Prints first and last column full
                print('*', end = ' ')
            elif col == n // 2:             # Prints a full column at half n
                print('*', end = ' ') 
            else:
                print(' ', end = ' ')
        print()



def squareDiagonals(n): 
    'draw n x n square with an X shape evenly distributed'

    print ('Diagonals')
    
    for row in range(n):              # Outer row
        for col in range(n):          # Inner column - Creates a line everytime i in range(n)
            if row == 0 or row == n - 1:
                print('*', end = ' ')
            elif row == 0 or col == 0 or row == col:  # Where the index of the row meets, print *
                print('*', end = ' ')
            elif row + col == n - 1:                  # Reverse of above
                print('*', end = ' ')
            elif col == 0 or col == n - 1:
                print('*', end = ' ')
            else:
                print(' ', end = ' ')
        print()


def columnSum(lst):
    'sum the elements of a column'

    newLst = []
    
    for row in range(0, len(lst)):    
        s = 0
        for col in range(0, len(lst)):
            s = s + lst[col][row]
        newLst.append(s)
        #print (s)
            
    return newLst


def numLoops():
    'Outputs number of times through while loop'
    
    userNum = eval(input('Enter a number: '))

    # Validation loop so I didnt have to run it everytime I entered incorrect num. Worked nice so kept it
    while userNum < 1:               
        print('Invalid. Number must be greater than 0')
        userNum = eval(input('Enter a number: '))

    totalLoop = 0
    
    while userNum != 1:
        if userNum % 2 == 0:
            userNum = userNum // 2
        else:
            userNum = (userNum // 3) + 1
        #print (userNum)
        totalLoop = totalLoop + 1

    print('Total times through the loop: {}'.format(totalLoop))
    return


def numLetters():
    'Inputs n words from user and outputs percent of 3-letter words'

    totalWords = 0
    shortWords = 0

    while(True):
        word = input('Enter a word or return: ')
        if word != '':
            totalWords = totalWords + 1
            if len(word) == 3:
                shortWords = shortWords + 1
        else:
            break

    average = shortWords / totalWords
    percent = int(average * 100)
    
    print()
    print('Total number of words: {} \nPercentage of 3-Letter words: {}%'.format(totalWords, percent))
    return
    
        
    
