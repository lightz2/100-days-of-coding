import random
# this is going to take input and convert it to a list
names_of_people = input("Give everybody's names seperated by comma. ")
names = names_of_people.split(", ")

person = random.choice(names)
print(person + " is going to pay for the meals today!")