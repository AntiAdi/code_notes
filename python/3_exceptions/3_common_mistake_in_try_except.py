"""
    I/P : 50
    O/P : x is 50

    I/P : 13.4
    O/P : NameError: name 'x' is not defined

    I/P : cat
    O/P : NameError: name 'x' is not defined
"""

try :
    x = int(input())
except ValueError :
    print("x is not integer")

print("x is", x)