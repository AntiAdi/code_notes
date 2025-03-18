import random

my_list = [a for a in range(1,101)]

n = int(input("How many numbers to pick from 1 to 100 ? : "))


#Repetition is allowed.
print("Repetition allowed :")
for i in range(n) :
    print(f"\tNumber {i+1} : {random.choice(my_list)}")

#Alternate.
    #print(random.choices(my_list, k=n))


#Repetition NOT allowed.
print("Repetition NOT allowed :")
for i in range(n) :
    choice = random.choice(my_list)
    my_list.remove(choice)
    print(f"\tNumber {i+1} : {choice}")
