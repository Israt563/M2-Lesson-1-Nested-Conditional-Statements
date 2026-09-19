# String Reverser
# File  : string_reverser.py

print("====================================")
print("      Welcome to String Reverser!   ")
print("====================================")
print()

# Input a word or sentence
user_string = input("Please enter your own string: ")
print()

reversed_string = ""

print("--- Reversing Process ---")
# Loop through each character to reverse it
for char in user_string:
    reversed_string = char + reversed_string
    print(f"Adding '{char}' -> Current result: {reversed_string}")

print()
print("====================================")
print(f" The Original String = {user_string}")
print(f" The Reversed String = {reversed_string}")
print("====================================")