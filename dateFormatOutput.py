# Name: Steven Rivera
# Simple Python program for date/time output formats

import time

class Date:

    
    def __init__(self):
        'intializes a new date and time to current date and time'
        self.date = time.localtime()

    def display(self, frmt):
        'using dictionary to store formats. I hope this is what you wanted (deceptively tricky problem!)'

        fullYear  = time.strftime('%Y', self.date)
        partYear  = time.strftime('%y', self.date)
        fullMonth = time.strftime('%m', self.date)
        partMonth = time.strftime('%b', self.date)
        day       = time.strftime('%d', self.date)

        output =  {'MDY' : '{}/{}/{}'.format(fullMonth, day, partYear),
                   'DMY' : '{}/{}/{}'.format(day, partMonth, partYear),
                   'DMYY': '{}/{}/{}'.format(day, partMonth, fullYear),
                   'MDYY': '{}/{}/{}'.format(partMonth, day, fullYear),
                   'MODY': '{} {},{}'.format(partMonth, day, fullYear)}
        

        #return frmt
        return output[frmt]

def test():
    x = Date()

    print(x.display('MDY'))
    print(x.display('DMY'))
    print(x.display('DMYY'))
    print(x.display('MDYY'))
    print(x.display('MODY'))

if __name__ == "__main__":
    test()
            




    

