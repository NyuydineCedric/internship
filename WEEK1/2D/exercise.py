i=int(input("Enter number: "))
while i<=30:
    if i%3==0 and i%5 == 0:
        print("FizzBuzz")
        print(i)
    elif i%3 ==0:
        print("Fizz")
        print(i)
    elif i%5 ==0:
        print("Buzz")
        print(i)
    
    i+=1