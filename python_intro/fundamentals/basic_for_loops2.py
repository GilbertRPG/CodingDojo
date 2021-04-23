# Biggie Size - Given a list, write a function that changes all 
# positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values 
# are now [-1, "big", "big", -5]

print("Biggie Size")
def bigNumber (numbers):
    big = []
    for i in numbers:
        if i > 0:
            i = "big"
            big.append(i)
        else:
            big.append(i)
    return big

print(bigNumber([-1,3,4,-5]))

# Count Positives - Given a list of numbers, create a function to replace the last value 
# with the number of positive values. (Note that zero is not considered to be a 
# positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and 
# returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] 
# and returns it

print("Count Positives")
# we're going to compare if the current number is higher than 0, and if so, add it to a "counter" table to hold the data.
def replacePositives (numbers):
    counter = 0
    for i in numbers:
        if i >= 0:
            counter += 1
    numbers[len(numbers) - 1] = counter # this gets you the last vaule of the list
    return numbers

print(replacePositives([-3,5,6,3,-6,-3,9]))

print("Sum Total")
# Sum Total - Create a function that takes a list and returns the sum of all the values in 
# the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

def totalSum(numbers):
    
    return numbers

print(totalSum([1,2,3,4]))