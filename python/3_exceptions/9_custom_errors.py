class AgeError(Exception) :
    pass


try :
    age = int(input("Enter your age : "))
except ValueError:
    print("Not an integer !")
else :
    if age<=0 or age>120:
        raise AgeError
    else :
        print(f"Age is {age}")