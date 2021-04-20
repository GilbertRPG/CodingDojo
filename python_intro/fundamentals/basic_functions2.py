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