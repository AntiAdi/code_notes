import random

probability = 100.0

while True :
    n = int(input("Choose a number between 1 and 5 (both inclusive) : "))
    random_number = random.randint(1,5) 
    if random_number == n :
        print("Computer chose the same !")
        probability *= 0.2
        break
    else :
        print("Computer chose :",random_number, "\nTry Again !" )
        probability *= 0.8

print(f"Probability of this is = {probability:.2f}%")