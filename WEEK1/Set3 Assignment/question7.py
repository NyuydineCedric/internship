#NUMBER GUESSING GAME WITH HINTS

def guessing_game(secret_number, max_attempts):
    
    attempts = 0

    while attempts < max_attempts:

        guess = int(input("Enter your guess: "))
        attempts = attempts + 1

        if guess == secret_number:
            print("Correct!")
            break

        elif guess < secret_number:
            print("Too low")

        else:
            print("Too high")

    print("Attempts used:", attempts)


guessing_game(45, 5)