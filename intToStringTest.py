# Name: Steven Rivera
# Homework 2, Question 2


numString = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
numInt = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
operator = ['+', '-', '*', '/']



userInput = (input('Enter calculation to be performed, e.g. 5+9: '))

firstNum = int(userInput[0])
secondNum = int(userInput[2])


if userInput[1] in operator:

    if len(userInput) == 3:

        if userInput[0] not in numInt:
            print(userInput[0] + ' is not a valid number')
            
        if userInput[2] not in numInt:
            print(userInput[2] + ' is not a valid number')
            
        else:
            if userInput[1] == '+':
                userCalc = firstNum + secondNum
                print(numString[firstNum] + ' plus ' + numString[secondNum] + ' is ' + str(userCalc))
    
            elif userInput[1] == '-':
                userCalc = firstNum - secondNum
                print(numString[firstNum] + ' minus ' + numString[secondNum] + ' is ' + str(userCalc))
    
            elif userInput[1] == '*':
                userCalc = firstNum * secondNum
                print(numString[firstNum] + ' multiplied by ' + numString[secondNum] + ' is ' + str(userCalc))
    
            elif userInput[1] == '/':
                if userInput[2] == '0':
                    print('Division by zero is not allowed')
                else:
                    userCalc = firstNum / secondNum
                    print(numString[firstNum] + ' divided by ' + numString[secondNum] + ' is ' + str(userCalc))
    else:
        print(str(len(userInput)) + ' is not a valid length')
        
else:
    print(userInput[1] + ' is not a valid operator')
    
    

print('thanks for playing')


# TEST CASE 1
# Input 5+1
# Expected Result: five plus one is 6
# thanks for playing

# TEST CASE 2
# Input 1-8
# Expected Result: one minus eight is -7
# thanks for playing

# TEST CASE 3
# Input 8/0
# Expected Result: Division by zero is not allowed
# thanks for playing

# TEST CASE 4
# Input 8$9
# Expected Result: $ is not a valid operator
# thanks for playing
