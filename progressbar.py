'''once you have created this program, you can display progress bars in your other python programs
by running import progressbar and printing the string returned from progressbar.getprogressBar().'''

import random,time

BAR=chr(9608)  #character 9608 is //

def main():
    #Simulate a download:
    print('Progressbar simulation')
    bytesDownloaded=0
    downloadSize=4096
    while bytesDownloaded <downloadSize:
        #Download a random amount of bytes:
        bytesDownloaded +=random.randint(0,100)

        #Get the progress bar string for this amount of prorgress:
        barStr=getProgressBar(bytesDownloaded,downloadSize)

        #Dont print a newline at the end, and immediately flush the printed string to the screen:
        print(barStr, end='', flush=True)
        time.sleep(0.2)

        #print backspaces to move the text cursor to the line's start
        print('\b' *len(barStr),end='',flush=True)
def getProgressBar(progress,total,barWidth=40):
    '''Returns a string that represents a progress bar that has barWidht bars and has progressed progress amount of total amount'''

    progressBar=''  #The progress bar will be a string value.
    progressBar +='['  #Create the left end of the progress bar.

    #make sure that the amount of the progress is between 0 and total:
    if progress>total:
        progress=total
    if progress <0:
        progress=0

    #calculate the number of 'bars' to display:
    numberOfBars =int((progress/total) *barWidth)

    progressBar += BAR * numberOfBars  #Add the progress bar.
    progressBar+=' '* (barWidth-numberOfBars) #Add empty space.
    progressBar+=']' #Add the right end of the progress bar.

    #calculate the percentage complete:
    percentageComplete=round(progress/total*100,1)
    progressBar+=' '+str(percentageComplete) + '%' #Add percentage.

    #Add the numbers:
    progressBar += '  ' + str(progress) + '/' +str(total)

    return progressBar  #return the progress bar string.
if __name__=='__main__':
    main()