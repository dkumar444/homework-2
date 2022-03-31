from datetime import date
import fileinput
my_file = open("parsedDates.txt", "w")
arr = ["January", "january", "February", "february", "March", "march", "April",
    "april", "May", "may", "June", "june", "July", "july", "August", "august",
    "September", "september" "October", "october", "November", "november",
    "December", "december"]

nums=[1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12]

def checkDateValidity(line)->bool:
    mc = 0
    for i in line:
            while mc!=23:
                s=arr[mc]

                #check to find if the month is correct or not
                if line.find(s) != -1:
                #check if the date has two digits
                        if line[len(s)+1].isdigit() and line[len(s)+2].isdigit():
                            if line[len(s)+3].isdigit()==False:
                                if line[len(s) + 1] <= '3' and line[len(s)+1]>='0':
                                    if line[len(s) + 2] <= '9' and line[len(s) + 2] >= '0':
                                         if line[len(s) + 1]!='3':
                                                #print("jany do")
                                                return True
                                         if line[len(s)+2]=='1' or line[len(s)+2] == '0':
                                                #print("jany do")
                                                return True
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                #means date is only one digit value
                        elif line[len(s)+1].isdigit():
                                if line[len(s)+2] == ',':
                                   if line[len(s) + 1] <= '9' and line[len(s)+1] >= '0':
                                      #print("jany do")
                                      return True
                        else:
                            return False
                mc+=1

def setInFile(line):
    Year = int(line[len(line) - 5:len(line)])
    #print(Year)
    if line[len(line) -9].isdigit()==True and line [len(line) -8].isdigit() ==True:
            #print(line[len(line) -9],line [len(line) -8])
            DATE = int(line[len(line) -9:len(line) -7])
    elif line[len(line) -8].isdigit()==True:
            #print(line [len(line) -8])
            DATE = int(line[len(line) - 8:len(line) - 7])


    i = 0
    while line[i] != " ":
        i += 1

    cmpD = line[: i]

    i = 0

    while arr[i] != cmpD:
        i += 1

    substr1=str(DATE)
    substr2=str(Year)
    my_file.write(substr1 +"/"+ str(nums[i]) + "/" + substr2+"\n")

def compare(line,D) -> bool:

    Year = int(line[len(line)-5:len(line)])
    today = int(D[len(D) - 4:len(D)])

    if today > Year:
        return True

    if line[len(line) -8] and line [len(line) -7]:
        DATE = int(line[len(line) -9:len(line) -7])
    elif  line[len(line) -7]:
        DATE = int(line[len(line) - 8:len(line) - 7])



    today = int(D[len(D) - 7:len(D)-5])

    if today > DATE:
        return True
    else:
        return False

    i=0
    while line[i]!=" ":
        i+=1

    cmpD = line[: i]

    i=0
    while D[i] != " ":
        i += 1
    today = D[: i]

    i=0

    while arr[i]!=cmpD:
        i+=1

    j=0
    while arr[j] != today:
        j += 1

    if(nums[i] < nums[j]):
        return True

    return False

def readfile(D):
    for line in fileinput.input(files='python.txt'):
        if line != '-1':

            if checkDateValidity(line) == True:
                if compare(line,D) == True:
                    print(line)
                    setInFile(line)


        else:
            break

if __name__ == '__main__':

    dateToday = date.today()
    D = dateToday.strftime("%B %d,%Y")
    readfile(D)





