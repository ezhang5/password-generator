# Date created: 7/19/19
# User: Eugenia Zhang
# Project: Protective Password Generator

import random

'''Task 1: Determine if the figures given by user input is valid or not.'''
    
def letterMath(numChar, numCapital, numNum, numSpecial):
    if numChar < (numCapital + numNum + numSpecial):
        return "ERROR: Numbers not valid. Please input correct values."
    
    
'''Task 3: Method to store randomized values into SOME STRUCTURE, 
combine the letters together, and then print out a message.'''

def createPassword(numChar, numCapital, numNum, numSpecial):
    
    # Create structure for password and create counters for limitations
    charCounter = 0
    capitalCounter = 0
    numberCounter = 0
    specialCounter = 0
    pwdList = []
    
    
    # Use random generator and counters to decide letters, numbers, and 
    # special characters that will be used and add them to pwdList.
    while numberCounter < int(numNum):
        pwdList.append(random.choice('1234567890'))
        numberCounter += 1
        charCounter += 1
    while capitalCounter < int(numCapital):
        pwdList.append(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        capitalCounter += 1
        charCounter += 1
    while specialCounter < int(numSpecial):
        pwdList.append(random.choice('!@#$%^&*()_+`~-=[]\{}|;:",./<>?'))
        specialCounter += 1
        charCounter += 1
    while charCounter < int(numChar):
        pwdList.append(random.choice('abcdefghijklmnopqrstuvwxyz'))
        charCounter += 1
        
    
    # Randomize the decided characters (think about how)
    random.shuffle(pwdList)
    
    # Return the new password
    return 'Your new protective password is: ' + ''.join(pwdList).strip('[]')


#******************************************************************************
# TESTING CODE
#******************************************************************************

if __name__ == "__main__":
    
    '''Task 1: Create variables to store user input. Will ask for: minimum number 
    of characters,minimum number of capital letters, minimum number of numbers, and
    minimum number of special characters.'''

    minChar = raw_input('What is the minimum number of characters required?' \
    + "If there is no limit, please enter 0.")
    minCapital = raw_input('What is the minimum number of capital letters ' \
    + "required? If there is no limit, please enter 0.")
    minNum = raw_input('What is the minimum number of numbers ' \
    + "required? If there is no limit, please enter 0.")
    minSpecial = raw_input('What is the minimum number of special characters ' \
    + "required? If there is no limit, please enter 0.") 
    print(createPassword(minChar, minCapital, minNum, minSpecial))
    
    
    
    
    