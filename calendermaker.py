'''This program generates a printable text files of monthly calendars for the month and year that
you enter'''

"""Create monthly calendars saved to a text and fit for printing"""

import datetime
#set up constants

DAYS=('SUNDAY','MONDAY','TUESDAY','WEDNSDAY','THURSDAY','FRIDAY','SATURDAY')
MONTHS=('JANUARY','FEBUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER')

print('CALENDER MAKER')
while True: #loop to get the year from the user
    print('Enter the year for the calendar')
    response=input('>?')

    if response.isdecimal() and int(response)>0:
        year=int(response)
        break
    print('Enter a numeric year, like 2023')
    continue
while True: #loop to get a month from the user
    print('Enter the month for the calendar:')
    response=input('>?')

    if not response.isdecimal():
        print('Please enter a numeric month like 3 for march')
        continue
    month=int(response)
    if month<=1 and month<=12:
        break
    print('Please enter a number from 1 to 12')
def getCalendar(year,month):
    calText=''  #This will contain the string of our calendar

    #Put the month and year at the top of the calendar
    calText+=(' '*34) + MONTHS[month-1] + ' ' + str(year) + '\n'

    #Add the days of the week labels to the calendar
    calText += 'sunday.....monday.....tuesday.....wednsday.....thursday.....friday.....saturday..\n'

    #The horizontal line string that separate weeks
    weekSeparator=('+--------------' * 7) +'\n'

    #The blank rows have ten spaces in between | day separators
    blankRow=('|       '*7) + '\n'

    #get the first date in the month
    currentDate=datetime.date(year,month)
    #Roll back until the current date is a sunday. (weekday()) retuns 6 for sunday not 0
    while currentDate.weekday() !=6:
        currentDate -=datetime.timedelta(days=1)

    while True: #loop over each week in the month
        calText+=weekSeparator
        #Daynumberrow is the row with the day number labels
        dayNumberRows=''
        for i in range(7):
            dayNumberLabel=str(currentDate.day).rjust(2)
            dayNumberRows += '|' +dayNumberLabel + ('' *8)
            currentDate += datetime.timedelta(days=1)  #go to next day
        dayNumberRows += '\n'  #add vertical line after saturday
        #Add the day number row and 3 blank rows to the calendar text
        calText += dayNumberRows
        for i in range(3):
            calText += blankRow
        #Check if we are done with the month
        if currentDate.month !=month:
            break

        #Add horinzontal line at the bottom of the calendar
        calText +=weekSeparator
        return calText
calText=getCalendar(year,month)
print(calText)
#save the calendar to a text file
calendarFileName='calendar _{}_{}.txt'.format(year,month)
with open(calendarFileName,'W') as fileObj:
    fileObj.write(calText)
print('Save to ' + calendarFileName)

