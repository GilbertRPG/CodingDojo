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