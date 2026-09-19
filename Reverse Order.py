# Countdown Timer
# File  : countdown.py

print("====================================")
print("      Welcome to Countdown!         ")
print("====================================")
print()

# Input number greater than 1
n = int(input("Enter the value of n (greater than 1): "))
print()

if n > 1:
    print(f"Numbers from {n} down to 1 are:")
    print("-" * 30)
    
    # Loop to print numbers in reverse
    for i in range(n, 0, -1):
        print(f"Count: {i}")
        
    print("-" * 30)
    print("Liftoff! 🚀")
else:
    print("Oops! Please enter a number greater than 1.")

print()
print("====================================")
print("   Countdown complete!              ")
print("====================================")