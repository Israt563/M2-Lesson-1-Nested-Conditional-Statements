# Assignment: Number Guessing Game
# File  : number_guessing_game.py

import random

print("====================================")
print("   Welcome to Number Guessing Game! ")
print("====================================")
print()

# Generate a random secret number between 1 and 100
secret_number = random.randint(1, 100)
attempts = 0

print("I have chosen a secret number between 1 and 100.")
print("Can you guess what it is? Let's find out! 🎲")
print("-" * 36)
print()

# Main game loop
while True:
    try:
        guess = int(input("Enter your guess (1-100): "))
        attempts += 1
        print()
        
        # Check the user's guess against the secret number
        if guess < secret_number:
            print("📈 Too low! Try a higher number.\n")
        elif guess > secret_number:
            print("📉 Too high! Try a lower number.\n")
        else:
            print("🎉 Congratulations! You guessed the secret number!")
            break
            
    except ValueError:
        print("❌ Invalid input! Please enter a valid whole number.\n")

# End-of-game summary report
print("====================================")
print("========== GAME SUMMARY ============")
print("====================================")
print(f"Secret Number   : {secret_number}")
print(f"Total Attempts  : {attempts}")
print("====================================")
print("Thanks for playing the game! 🌟")
print("====================================")