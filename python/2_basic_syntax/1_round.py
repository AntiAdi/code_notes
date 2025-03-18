num1 = 123456.123456

print("\n\tNumber = ", num1)

print(
    """ 
        Input:

    round(number=num1, ndigits=-3)
    round(number=num1, ndigits=-2)
    round(number=num1, ndigits=-1)
    round(number=num1, ndigits= 0)
    round(number=num1, ndigits= 1)
    round(number=num1, ndigits= 2)
    round(number=num1, ndigits= 3)

        Output :      
""", end="\n\t"
)

print(
    round(number=num1, ndigits=-3),
    round(number=num1, ndigits=-2),
    round(number=num1, ndigits=-1),
    round(number=num1, ndigits= 0),
    round(number=num1, ndigits= 1),
    round(number=num1, ndigits= 2),
    round(number=num1, ndigits= 3), sep="\n\t"
)