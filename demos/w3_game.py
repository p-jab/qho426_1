import random #Taking definitions from package "random" into this scope
secret = random.randint(1,20)
print("Welcome to my Guess-Game. I am thinking of number between 1 and 20")

for attempt in range(5):
    print(f"Attempt nr {attempt+1}")
    try:
        guess = int(input("Take a guess: "))
        if guess not in range(1,21):
            print("Wrong guess. Number is between 1 and 20")
        else:
            if guess == secret:
                print("Congrats! You won the game, bro!")
                break
            elif guess > secret:
                print("Too high!")
            elif guess < secret:
                print("Too low!")
    except Exception:
        print("Not a number")
if guess != secret:
    print(f"Game over, looser! My number was {secret}")