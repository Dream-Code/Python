# Name: Steven Rivera
# This program will take a word from user and output the Pig-Latin variation of that word

# Holding the vowel values
vowels = ['a', 'e', 'i','o', 'u']

userWord = input('Enter word: ')

# Holding first letter of input to both store and check value for output
firstLetter = userWord[0]


if firstLetter in vowels:                                   # Checking if word starts with vowel == True
    print('Word: ' + userWord)
    print('In Pig-Latin: ' + userWord + 'yay')
else:                                                       # Default if above != True
    userWord = userWord[1:]
    print('Word: ' + userWord)
    print('In Pig-Latin: ' + userWord + firstLetter + 'ay')
    

# TEST CASE 1
# Word: gypsy
# Predicted result: ypsygay

#TEST CASE 2
# Word: integer
# Predicted result: integeryay
