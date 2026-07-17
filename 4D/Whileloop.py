# name=input("Enter your name: ")
# while name == "":
#     print("You have not entered your name!")
#     name = input("Enter your name: ")
# print(f"Hello {name}")
#------------------------------------------------------------

# age = int(input("Enter your age: "))

# while age<0:
#     print("Age cannot be negative")
#     age = int(input("Enter your age: "))
    
# print (f"You are {age} years old")

#--------------------------------------------------------------

# food = input("Enter a food you like (press q to quit): ")
# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter another food you like (press q to quit): ")
# print("bye")

#-------------------------------------------------------------------

num = int(input("Enter a number between 1 to 10: "))

while num < 1 or num >10:
    print (f"{num} is not valid")
    num = int(input("Enter a number between 1 and 10: "))
    
print (f"Your number is {num}")