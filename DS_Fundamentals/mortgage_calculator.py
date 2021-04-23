p = 400000 #principal
r = 0.25 #interest rate/12
n = 360 #term length

def mortgageCalculator():
    result = p * r* (1+r)**n / (1+r)**n - 1 # Object not Callable fix: float was seen as a function call so a * was needed.
    return result

print(mortgageCalculator())