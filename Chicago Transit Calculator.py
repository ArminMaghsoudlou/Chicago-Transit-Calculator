

def baseFare(fareType, fareCat):
    ''' Take the fare type and fare category as parameters and returns the corresponding CTA fare. '''
    returnValue = -1
    if fareType == 'L train fare' and fareCat == 'Full':
        returnValue = 2.50
    elif fareType == 'L train fare' and fareCat == 'Reduced':
        returnValue = 1.25
    elif fareType == 'L train fare' and fareCat == 'Student':
        returnValue = 0.75
    elif fareType == 'Bus fare' and fareCat == 'Full':
        returnValue = 2.25
    elif fareType == 'Bus fare' and fareCat == 'Reduced':
        returnValue = 1.10
    elif fareType == 'Bus fare' and fareCat == 'Student':
        returnValue = 0.75
    elif fareType == 'Transfer' and fareCat == 'Full':
        returnValue = 0.25
    elif fareType == 'Transfer' and fareCat == 'Reduced':
        returnValue = 0.15
    elif fareType == 'Transfer' and fareCat == 'Student':
        returnValue = 0.15
    elif fareType == 'Free' and fareCat == 'Free':
        returnValue = 0.00
    elif fareType == 'Bus fare cash' and fareCat == 'Full':
        returnValue = 2.50
    elif fareType == 'Bus fare cash' and fareCat == 'Reduced':
        returnValue =  1.25
    elif fareType == 'Bus fare cash' and fareCat == 'Student':
        returnValue = 0.75
    elif fareType == 'Ohare L train' and fareCat == 'Full':
        returnValue = 5.00
    elif fareType == 'Ohare L train' and fareCat == 'Reduced':
        returnValue = 1.25
    elif fareType == 'Ohare L train' and fareCat == 'Student':
        returnValue = 0.75
    elif fareType == '128 Soldier Field Express' and (fareCat == 'Full' or fareCat == 'Student'):
        returnValue =  5.00
    elif fareType == '128 Soldier Field Express' and fareCat == 'Reduced':
        returnValue = 2.50
    return returnValue

def passPrice(passType, fareCat):
    ''' Takes the pass type and fare category as parameters and returns the corresponding pass price. '''
    if passType == '1-Day CTA Pass' and (fareCat == 'Full' or fareCat == 'Reduced' or fareCat == 'Student'):
        return 10.00
    elif passType == '3-Day CTA Pass' and (fareCat == 'Full' or fareCat == 'Reduced' or fareCat == 'Student'):
        return 20.00
    elif passType == '7-Day CTA Pass' and (fareCat == 'Full' or fareCat == 'Reduced' or fareCat == 'Student'):
        return 28.00
    elif passType == '7-Day CTA/Pace Pass' and (fareCat == 'Full' or fareCat == 'Reduced' or fareCat == 'Student'):
        return 33.00
    elif passType == '30-Day CTA/Pace Pass	' and (fareCat == 'Full' or fareCat == 'Student'):
        return 105.00
    elif passType == '30-Day CTA/Pace Pass' and (fareCat == 'Reduced'):
        return 50.00
    return -1

def askGeneralQuestions():
    '''This function asks the user some general questions and returns the appropriate fare type and fare category. '''
    global fareCat
    fareCat = 'Full'
    global numTickets
    while True:
        try:
            numTickets = int(input('How many tickets do you want to purchase?\n'))
        except (ValueError):
            print('Please enter a valid integer.')
        else:
            if numTickets < 1:
                print('To use this calculator you need to purchase at least 1 ticket.')
            else:
                fareType = input('Will you be taking thr L train or the bus?\nType "L" for L train or "B" for bus:\n')
                transferBool = input('Have you taken the train or bus within the past 2 hours?\nType Yes or No:\n')
                if transferBool.upper() == 'YES':
                    transferBool = True
                elif transferBool.upper() == 'NO':
                    transferBool = False
                if transferBool == False:
                    if fareType.upper() == 'L':
                        fareType = 'L train fare'
                    elif fareType.upper() == 'B':
                        fareType = 'Bus fare'
                else:
                    fareType = 'Transfer'
                ohareBool = input("Are you travelling from O'Hare station? Type Yes or No:\n")
                if ohareBool.upper() == 'YES':
                    ohareBool = True
                elif ohareBool.upper() == 'NO':
                    ohareBool = False
                if ohareBool == True:
                    soldierBool = input('Are you taking the 128 Soldier Field Express? Type Yes or No:\n')
                    if soldierBool.upper() == 'YES':
                        soldierBool = True
                        fareType = '128 Soldier Field Express'
                    elif soldierBool.upper() == 'NO':
                        soldierBool = False
                        fareType = 'Ohare L train'
                upassBool = input('Do you have a U-Pass? Type Yes or No:\n')
                if upassBool.upper() == 'YES':
                    upassBool = True
                    fareType = 'Free'
                    fareCat = 'Free'
                elif upassBool.upper() == 'NO':
                    upassBool = False
                if upassBool == False:
                    riderAge = int(input('How old are you?\n'))
                    if riderAge < 7:
                        fareType = 'Free'
                        fareCat ='Free'
                    else:
                        if riderAge >= 65:
                            seniorBool = input('Are you currently enrolled in the Illinois Department on Aging’s Benefit Access Program? Type Yes or No:\n')
                            if seniorBool.upper() == 'YES':
                                seniorBool = True
                                fareType = 'Free'
                                fareCat = 'Free'
                            elif seniorBool.upper() == 'NO':
                                seniorBool = False
                                fareCat = 'Reduced'
                        if riderAge > 6 and riderAge < 12:
                            fareCat = 'Reduced'
                        else:
                            if riderAge < 20 and riderAge > 11:
                                studentBool = input('Are you an elementary or high school student? Type Yes or No:\n')
                                if studentBool.upper() == 'YES':
                                    studentBool = True
                                    timeToday = input('What time do you want to travel? Enter using military time (24 hour clock):\n')
                                    dayToday = input('What day of the week do you want to travel?\n')
                                    timeToday = float(timeToday.replace(':','.'))
                                    dayToday = dayToday.upper()
                                    if (timeToday >= 5.3) and (timeToday <= 20.3) and (dayToday != 'SATURDAY' or dayToday != "SUNDAY"):
                                        fareCat = 'Student'
                                    else:
                                        fareCat = 'Full'
                                elif studentBool.upper() == 'NO':
                                    studentBool = False
                            milBool = input('Are you an active U.S. military personnel? Type Yes or No:\n')
                            if milBool.upper() == 'YES':
                                milBool = True
                                fareCat = 'Free'
                                fareType = 'Free'
                            elif milBool.upper() == 'NO':
                                milBool = False
                                disabilityBool = input('Do you have a disability? Type Yes or No:\n')
                                if disabilityBool.upper() == 'YES':
                                    disabilityBool = True
                                    fareCat ='Reduced'
                                elif disabilityBool.upper() == 'NO':
                                    disabilityBool = False
                                if disabilityBool == True and riderAge < 65:
                                    seniorBool = input('Are you currently enrolled in the Illinois Department on Aging’s Benefit Access Program? Type Yes or No:\n')
                                    if seniorBool.upper() == 'YES':  #seniorBool does not refer to the customer being a senior or not. it refers to them being enrolled in the Benefit access program or not.
                                         seniorBool = True
                                         fareCat = 'Free'
                                         fareType = 'Free'
                                    elif seniorBool.upper() == 'NO':
                                         seniorBool = False
                            if (fareType == 'Bus fare') and (fareCat != 'Free'):
                                payMethod = input('Are you paying with cash? Type Yes or No:\n')
                                if payMethod.upper() == 'YES':
                                    payMethod = True
                                    fareType = 'Bus fare cash'
                                elif payMethod.upper() == 'NO':
                                    payMethod = False
                lstFare = [fareType,fareCat]
                return lstFare

def calcPrice():
    '''Calculates fare price '''
    lstFare = askGeneralQuestions()
    fareType = lstFare[0]
    fareCat = lstFare[1]
    return baseFare(fareType,fareCat)

def askAboutPass():
    '''Asks the user if they are interested in a pass. If yes, the function will return the pass type they are interested in.'''
    if fareCat != 'Free':
        global passType
        passType = ''
        passTypeList = ['1-Day CTA Pass', '3-Day CTA Pass', '7-Day CTA Pass', '7-Day CTA/Pace Pass', '30-Day CTA/Pace Pass']
        passPrint = ''
        for item in passTypeList:
            passPrint = passPrint + '\n' + item
        global passContinue
        while True:
            passContinue = input('The following passes are available. Do any of the following interest you?\n' + passPrint + '\n\nType Yes or No:\n')
            if passContinue.upper() != 'YES' and passContinue.upper() != 'NO':
                print('Please type Yes or No')
            else:
                if passContinue.upper() == 'YES':
                    passContinue = True
                    try:
                        passTypeNum = int(input('Type 1 for a 1-day pass\n3 for a 3-day pass\n7 for a 7-day pass\nor 30 for a 30-day pass:\n'))
                    except (ValueError):
                        print('Please enter an integer')
                    else:
                        if passTypeNum == 7:
                            pacePassBool = input('Do you want a pace pass as well?\nType Yes or No:\n')
                            if pacePassBool.upper() == 'YES':
                                pacePassBool = True
                            elif pacePassBool.upper() == 'NO':
                                pacePassBool = False
                        if passTypeNum == 1:
                            passType = '1-Day CTA Pass'
                        elif passTypeNum == 3:
                            passType = '3-Day CTA Pass'
                        elif (passTypeNum == 7) and (pacePassBool == False):
                            passType = '7-Day CTA Pass'
                        elif (passTypeNum == 7) and (pacePassBool == True):
                            passType = '7-Day CTA/Pace Pass'
                        elif passTypeNum == 30:
                            passType = '30-Day CTA/Pace Pass'
                        return passType
                elif passContinue.upper() == 'NO':
                     passContinue = False
                     return


def startProgram():
    '''Tells the user how much his/her tickets will be depending on the number of tickets he/she wants to buy'''
    userCost = calcPrice()
    userTotalCost = userCost * numTickets
    if numTickets == 1:
        print('Your fare will be $' + str(userCost))
    else:
        print('One ticket will cost you ${} \nFor {} tickets, your total cost is ${}'.format(userCost,numTickets, userTotalCost))
    if fareCat != 'Free':
        askAboutPass()
        if passContinue == True:
            passCost = passPrice(passType,fareCat)
            totalPassCost = passCost * numTickets
            print('One {} will cost ${}\nFor {} passes, your total cost would be ${}'.format(passType,passCost,numTickets, totalPassCost))
    return

startProgram()

