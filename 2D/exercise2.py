#Counting number digits
num=int(input("Enter a number: "))
num=[int(x) for x in str(num)]
print("Number of digits:", len(num))
