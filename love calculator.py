print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


# lower_case_name = name1.lower()
# lower_case_name.count("t")
add_name = name1.lower() + name2.lower()
true1 = add_name.count("t")
true2 = add_name.count("r")
true3 = add_name.count("u")
true4 = add_name.count("e")
total_true = int(true1 + true2 + true3 + true4)
# print(total_true)
love1 = add_name.count("l")
love2 = add_name.count("o")
love3 = add_name.count("v")
love4 = add_name.count("e")
total_love = int(love1 + love2 + love3 + love4)
total = str(total_true) + str(total_love)
love_score = int(total)
if love_score <= 10 or love_score >= 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.") 
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print (f"Your score is {love_score}.")        
