#Use else
try :
    x = int(input())
except ValueError :
    print("x is not integer")
else :
    print("x is", x)