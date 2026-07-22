from fastapi import FastAPI
app=FastAPI()

@app.get("/fizzbuzz/{number}")
def fizzbuzz(number:int):
    result=[]

    
    while number<=30:
        if(number%3==0 and number%5==0):
            result.append({"type":"fizz_buzz","number":number})
            
        elif (number%3==0):
            result.append({"type":"fizz","number":number})
            print(number)
        elif(number%5==0):
            result.append({"type":"buzz","number":number})

        number+=1
    return {"result":result}