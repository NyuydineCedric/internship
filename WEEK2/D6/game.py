from fastapi import FastAPI

app = FastAPI()

secretNumber = 7

@app.get("/guess/{guess}")
def guess_number(guess: int):
    if guess < secretNumber:
        return {"message": "Too low"}
    elif guess > secretNumber:
        return {"message": "Too high"}
    else:
        return {"message": "You guessed it right! Congrats!"}