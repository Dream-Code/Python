# Name: Steven Rivera
# Python program to track a student meal account balance

class MealCard:
    'Track meal account allowing purchases, adding to card and balance queries'
    minBalance = 0
    
    def __init__(self, numPoints = 0):
        'creates student meal card object with an initial balance of 0'
        self.student = numPoints

    def purchaseFood(self, numPoints):
        'uses current balance for purchases, exceptions for less than/equal to 0 balance'
        balance = self.balance()
        balance = self.student - numPoints
        
        if int(balance) <= MealCard.minBalance:
            raise ValueError('Insufficient funds')
        
        else: # numPoints < int(balance): 
            balance = self.student = self.student - numPoints

    def addPoints(self, numPoints):
        'Adds funds to card specified by user'
        self.student += numPoints

    def balance(self):
        'returns balance when called'
        return 'Available points: {:5.2f}'.format(self.student)
        

    def __repr__(self):
        'canonical representation of the constructor'
        return 'Your point balance is: {:5.2f}'.format(self.student)

def test():
    'Test function for MealCard()'
    amt = eval(input('Enter initial balance: '))
    user = MealCard(amt)
    value = input('Enter D, P, or B: ')

    while value in ['D', 'P', 'B']:
        if value == 'D':
            amt = eval(input('Enter deposit amount: '))
            user.addPoints(amt)
            print(user)
        elif value == 'P':
            amt = eval(input('Enter purchase amount: '))
            try:
                user.purchaseFood(amt)
            except ValueError:
                print('Purchases are not allowed at this time. ' +
                      '\nTo make purchases, minimum balance is required')
        elif value == 'B':
            print(user.balance())

        value = input('Enter D, P or B: ')
    print('Goodbye.')
        

if __name__ == "__main__":
    test()
            
