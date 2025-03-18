"""
    while True :
        try :
            x = int(input("Enter an integer : "))
        except ValueError :
            print("Not an integer. Try again !")
        else :
            print("x is ", x, sep="")
            break
"""


"""
    def get_int() :
        while True :
            try :
                x = int(input("Enter an integer : "))
            except ValueError :
                print("\tNot an integer. Try again !")
            else :
                return x
"""

def get_int() :
    while True :
        try :
            return int(input("Enter an integer : "))
        except ValueError :
            print("\tNot an integer. Try again !")


print(get_int())