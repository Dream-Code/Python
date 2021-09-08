# Name: Steven Rivera
# Python program to take in .csv file with user info, requiring PIN to enter account
# provides options for account navigation once PIN has been validated

def startUp(fname):
    'Function to create dict from file in main'

    userInfo = {}
    #print(userInfo[0])
    
    try:
        infile = open(fname, 'r')
        lines = infile.readlines()              
        infile.close()
        #return lines

        for line in lines:              
            lst = line.split(',')              
            pin = lst[0]                      

            info = []                          
            for item in range(1, len(lst)):    
                info.append(lst[item])
                    
            userInfo[lst[0]] = lst[1:3] + [float(lst[3])]
            #userInfo[pin] = info

        return userInfo

    except IOError:
        print('Cannot get to the file')
        return None
  


def getUser(tempDict):
    'Taking pin input from dictionary, validating pin and returning the key/value pair pin and name'
    while True:
        userPin = input('Welcome -- Enter a pin number: ')

        if len(userPin)  == 4 and userPin in tempDict:

            tempList = []
            for key in tempDict:
                if key == userPin:
                    tempList.append(tempDict[key])

            name = tempList[0][0]
            pin = userPin

            return pin, name
            
        
        else:
            print('Incorrect pin')
            return None, None      # This doesn't seem to do anything

def menu(name):

    try: 

        print('{}:'.format(name))
        print('1: {}:'.format('Deposit'))
        print('2: {}:'.format('Withdraw'))
        print('3: {}:'.format('Check Balance'))
        print('4: {}:'.format('My Data'))
        print('5: {}:'.format('Report'))
        print('6: {}:'.format('Quit'))
        print()

        userInput = eval(input('Enter number: '))
            
        if userInput < 1 or userInput > 6:
            print('Valid choices are 1, 2, 3, 4, 5, 6. Try again')
            
        else:
            return userInput
        

    except:
        print('Invalid character, try again')


    #return userInput
    


def getAmount():

    try:
        while True:
            userAmount = float(input('Enter Amount: '))

            if userAmount < 0:
                print('Negative Amount. Please try again')
            else:
                return userAmount

    except:
        print('Invalid amount. Use digits only')   


def deposit(pin, d):
    

    balance = d[pin][2]
    amount = getAmount()
    #print(balance)
    #print(type(balance))

    newBalance = balance + amount
    d[pin][2] = newBalance

    return

def withdraw(pin, d):

    balance = d[pin][2]
    amount = getAmount()
    #print(balance)
    #print(type(balance))

    while amount > balance:
        
        if amount == 0:
            break
        else:
            print('Insufficient funds to complete the transaction')
            amount = getAmount()


    if amount <= balance:
        newBalance = balance - amount
        print(newBalance)
        d[pin][2] = newBalance

    return


def balance(pin, d):

    balance = d[pin][2]

    return balance


def printUserData(pin, d):

    firstName = d[pin][0]
    lastName = d[pin][1]
    balance = d[pin][2]

    print('{} {} ${:.2f}'.format(firstName, lastName, balance))


def printReport(d):
    
    print ()
    print('Contents of Dictionary:')
    
    for pin in d:
        firstName = d[pin][0]
        lastName  = d[pin][1]
        balance   = d[pin][2]
        print('{:5} {:10} {:10} ${:12.2f}'.format(pin, firstName, lastName, balance))


def main():
    'Main method'
    
    dict = startUp('accounts.csv')
    
    if dict == None:
        return
    
    user, name = getUser(dict)
    
    if user != None and name != None:
        proceed = True

        while proceed:
            print()
            choice = menu(name)
            if choice == 1:
                deposit(user, dict)
            elif choice == 2:
                withdraw(user, dict)
            elif choice == 3:
                b = balance(user, dict)
                msg = 'Your current balance is ${:.2f}'
                print(msg.format(b))
            elif choice == 4:
                printUserData(user, dict)
            elif choice == 5:
                printReport(dict)
            elif choice == 6:
                proceed = False

    print('Goodbye')







    
