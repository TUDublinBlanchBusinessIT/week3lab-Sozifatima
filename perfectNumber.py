#SoziFatima
#07/02/2024
#perfectNumbers.py

from divisors import divisors 

def perfectNumber(x):
    result = False
    sum_of_divisors = sum(divisors(x))
    if sum_of_divisors == x:
        result = True
    return result

