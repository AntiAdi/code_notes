try:
    x = int(input("Enter a number: "))  # May cause ValueError
    print(10 / x)  # May cause ZeroDivisionError
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")