# Name: Steven Rivera
# Python program implementing a Caesar cipher

def caesar(num):

    alphaUpper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphaLower = 'abcdefghijklmnopqrstuvwxyz'
    shiftValue = num % 26
    joinedString = alphaLower + alphaUpper
    cipherString = ''
    
    for i in range(len(joinedString)):
        char = joinedString[i]
        
        # check for the lowerCase and UpperCase:
        #ord function gives the ascii value of the character.
        if char.isupper() == True:  # determine the character if it is upperCase or not.
            cipherString += chr((num - 65 + ord(char)) % 26 + 65) # logic for converting the character.
        else:# lowercase
            cipherString += chr((num-97 + ord(char)) % 26 + 97)
    
    return cipherString

def main():
    
    alphaUpper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphaLower = 'abcdefghijklmnopqrstuvwxyz'
    fullAlpha = alphaLower + alphaUpper
    
    userShift = int(input("Enter number of positions to shift to the right:  "))
    
    print('Normal: ' + fullAlpha)
    caesarText = caesar(userShift);
    print("Cipher: " + caesarText)
    print('')
    
    fileName = input("enter the file to be encrypted:  ")
    
    fileNames = fileName.split('.')
    outputFileName = fileNames[0] + "_ENC."+ fileNames[1]
    print("Encrypted file is ", outputFileName)
    
    
    # taking three variables:
    numberOfLines = 0
    numberOfCharacters = 0
    numberOfWords = 0

    
    # file opening.
    with open(fileName,'r') as rf: 
        # for writing the data into the file.
        with open(outputFileName,'w') as wf: # this is for writing into the file.
            for line in rf:
                numberOfLines = numberOfLines + 1
                table = line.maketrans(fullAlpha, caesarText, "") 
                encryptedLine = line.translate(table)
                wf.write(encryptedLine)
                splitLine = line.split(" ")
                print(splitLine)
                for item in splitLine:
                    if item == '\n':
                        continue
                    numberOfWords = numberOfWords + 1
                    numberOfCharacters = numberOfCharacters + len(item)
    
    
    # print the Statistics 
    print("Num Lines:",numberOfLines , "Num Chars:", numberOfCharacters , "Num Words:", numberOfWords)

    
###################################################
# THIS WAS A TEST FUNCTION TO TEST INITIAL OUTPUT #
###################################################
#def alphaShift(userShift):   

#    alphaUpper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#    alphaLower = 'abcdefghijklmnopqrstuvwxyz'
#    fullAlpha = alphaUpper + alphaLower
#    print('Normal: ' + fullAlpha)
#    caesarText = caesar(userShift);
#    print("Cipher: " + caesarText)
