print(
    """
    I/P : int("two")
    O/P : ValueError: invalid literal for int() with base 10: 'two'
    
    I/P : import math
          math.sqrt(-1)
    O/P : ValueError: math domain error

    I/P : import datetime  
          datetime.date(2025, 13, 5) #Incorrect arguments for a function
    O/P : ValueError: month must be in 1..12

    I/P : x,y = 1,2,3
    O/P : ValueError: too many values to unpack (expected 2)

    I/P : min([]) #Empty list
    O/P : ValueError: min() iterable argument is empty
"""
)