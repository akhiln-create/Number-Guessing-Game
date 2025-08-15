# This is a simple number guessing game.
# The computer picks a secret number, and you try to guess it!

secret_number = random.randint(1, 10)  # The secret number (fixed for simplicity as no external libraries allowed for true randomness)
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I have picked a number between 1 and 10. Can you guess it?")

while True:
    attempts += 1
    try:
        user_guess = int(input("Enter your guess: "))
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        continue

    if user_guess < secret_number:
        print("Too low! Try again.")
    elif user_guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
        break

print("Thanks for playing!")
