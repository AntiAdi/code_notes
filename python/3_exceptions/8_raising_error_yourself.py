try :
    age = int(input("Enter your age : "))
except ValueError:
    print("Not an integer !")
else :
    if age<=0 or age>120:
        raise ValueError("Invalid Age !")
    else :
        print(f"Age is {age}")