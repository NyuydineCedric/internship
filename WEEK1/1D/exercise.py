import random
number  = None
# if (number==7):
#     print("You guessed correctly")
# elif (number>7):
#     print("Number is too high")
# else:
#     print("Number is too low")

secret = random.randint(1,9)
while number != secret:
    number  = int(input("Enter a guess number"))
    if (number>secret):
        print("Number is high")
    elif (number<secret):
        print("Number is low")
    
print("congratulations")