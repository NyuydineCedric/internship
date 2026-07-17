# i=int(input("Enter a number: "))
num= int(input("Enter a another number"))
    
# def multiplication_table(i,num):
#     product = i*num
#     while num <=10:
#         print(f"{i} X {num} = {product}")
#         num = num+1
#         product = i*num
        
        
    
    
    


def multiplication_table(num):
    for i in range(1,11):
        product = num*i
        print(f"{num} X {i} = {product}")

multiplication_table(num)