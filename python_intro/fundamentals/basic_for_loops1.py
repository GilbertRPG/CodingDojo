# Basic - Print all integers from 0 to 150. Hint:use a for loop and range

for x in range(151):
    print("Basic Range to 150." , x)

# Multiples of Five - Print all the multiples of 5 from 5 to 1,000

for x in range(5, 1005, 5):
    print("Multipes of Five:" , x)

# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".

# if you have 2 #s, a and b and the quotient q = a/b, it is integer division then the remainder r is a - bq.
# Here is an example:
# a = 10
# b = 5
# q is the largest number where a - bq is not negative
# q = 2
# Formula: r = a - bq
# r = 0

for x in range(1, 101):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")
    else:
        print(x)

# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
print("BigNumber")
x = 1
total = 0
while x < 500000:
    total = total + x
    x = x + 2
print(total)

# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
print("Count_by_Four")
x = 2018
while x >= 0:
    print(x)
    x = x - 4

# Flexible Counter (optional) - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. 
# For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
print("FlexibleCounter")
lowNum = int(input("LowNumber "))
highNum = int(input("HighNumber "))
mult = int(input("Mult "))

while lowNum <= highNum:
    if lowNum % mult == 0:
        print(lowNum)
    lowNum = lowNum + 1
