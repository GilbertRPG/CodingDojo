print("Countdown")
def totalList(myNumber):
    
    list = []
    # myNumber = int(input("My Number "))
    while myNumber > 0:
        list.append(myNumber)
        # print(list)
        myNumber = myNumber - 1
    return list

print(totalList(int(input("My Number "))))

print("Print and Return")
def printReturn(a, b):
    list = []
    print(a)
    list.append(b)
    return list

print(printReturn(int(input("First Number to Print ")),(input("Second Number to Returned "))))
    #a = int(input("First Number to Print "))
    #b = int(input("Second Number to Returned "))