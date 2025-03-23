import random

print("Guess the correct secret number between 1 - 100")
secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 5  

while attempts < max_attempts:
    try:
        guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: Guess the secret number: "))
        if guess == secret_number:
            print("🎉 Congratulations! You guessed the correct number.")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
        attempts += 1
    except ValueError:
        print("Invalid input! Please enter a number.")

if attempts == max_attempts and guess != secret_number:
    print(f"😞 Sorry, you've used all your attempts. The secret number was {secret_number}.")
