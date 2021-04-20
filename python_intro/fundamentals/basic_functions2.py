def getList():
    list = []
    totalNumberCount = int(input("How many numbers? "))
    for i in range(totalNumberCount):
        # int(input("some numbers "))
        list.append(int(input("some numbers ")))
    return list

print("Countdown")
def totalList(myNumber):
    
    list = []
    while myNumber > 0:
        list.append(myNumber)
        myNumber = myNumber - 1
    return list

print(totalList(5))

print("Print and Return")
def print_and_return(userInput):
    print(userInput[0])
    return userInput[1]

print(print_and_return(getList()))

print("First plus Length")
# First Plus Length - Create a function that accepts a list 
# and returns the sum of the first value in the list plus the 
# list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 
# (first value: 1 + length: 5)

def first_plusLength(list):
    #list(range(int(input())))
    length = len(list)
    firstNumber = list[0]
    total = length + firstNumber
    return total

print(first_plusLength(getList()))

# This Length, That Value- Write a function that accepts two integers as 
# parameters: size and value. The function should create and return a list whose length 
# is equal to the given size, and whose values are all the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]
print("This Length, That Value")
def thisLengthThatValue(value1, value2):
    returnValue = []
    for i in range(value1):
        returnValue.append(value2)
    return returnValue

print(thisLengthThatValue(4, 7))

# Values Greater than Second (Optional) - Write a function that accepts a list and creates
# a new list containing only the values from the original list that are greater than its
# 2nd value. Print how many values this is and then return the new list. If the list has
# less than 2 elements, have the function return False
# 
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False
print("Vaules Greater Than Second")
def valueGreaterThanSecond(numbers):
    output = []
    if len(numbers) < 2:
        return False
    secondNumber = numbers[1]
    for i in numbers:
        if i > secondNumber:
            output.append(i)
    print(len(output))
    return output

print(valueGreaterThanSecond(getList()))