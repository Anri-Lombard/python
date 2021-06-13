"""
Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the
integer's divisors(except for 1 and the number itself), from smallest to largest.
If the number is prime return the string '(integer) is prime
'"""


def divisors(integer):
    factor_list = []
    for i in range(2, integer):
        if integer % i == 0:
            factor_list.append(i)
    if len(factor_list) > 0:
        return factor_list
    else:
        return f"{integer} is prime"


divisors(13)
