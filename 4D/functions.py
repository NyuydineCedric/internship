# def HappyBirthday(name, age):
#     print(f"Happy birthday to {name}")
#     print(f"You are {age} years old")
#     print("Happy birthday to you!")
#     print()

# HappyBirthday("Cedric", 20)
# HappyBirthday("Joe", 30)
# HappyBirthday("Jim", 40)

#-------------------------------------------------------------------

# def display_invoice(username, amount, due_date):
#     print(f"Hello {username}")
#     print(f"Your bill of {amount} is due: {due_date}")
# display_invoice("Cedric",20, "11/11")

#----------------------------------------------------------------------

# def Add(x,y):
#     z=x+y
#     return z

# def Subtract(x,y):
#     z=x-y
#     return z
# def Multiply(x,y):
#     z=x*y
#     return z
# def Divide(x,y):
#     z=x-y
#     return z

# print (Add(1,2))
# print (Subtract(1,2))
# print (Multiply(1,3))
# print (Divide(1,2))

#--------------------------------------------------------------

def create_name(first_name,last_name):
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    return first_name + " " + last_name

full_name = create_name("nyuydine", "cedric")

print(full_name)