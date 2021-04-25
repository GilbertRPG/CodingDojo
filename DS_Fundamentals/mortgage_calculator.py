p = 400000 # principal 
r = 0.0025 # interest rate per month
n = 360 # term length

def mortgageCalculator():
    result = (p * r * (1+r)**n) / ((1+r)**n - 1) # Object not Callable fix: float was seen as a function call so a * was needed.
    result2 = (2500000 * 0.088 * (1 + 0.088)**240) / ((1+0.088)**240-1) # Result2 is simply a longhanded test. I utilized this to calculate from some examples I found online to ensure the calculations were correct.
    return result, result2

print(mortgageCalculator())