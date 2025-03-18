import random

#Shuffling
my_list = [a for a in range(1, 11)]
print("Before Shuffling :", my_list)
random.shuffle(my_list)
print("After Shuffling :", my_list)

#Unique Choices
n = int(input("How many unique random integers you want ? : "))
print(random.sample(my_list, n))