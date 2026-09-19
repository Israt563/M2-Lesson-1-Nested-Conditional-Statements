# Half Pyramid Pattern Generator
# File  : half_pyramid.py

print("====================================")
print("    Welcome to Pyramid Generator!   ")
print("====================================")
print()

# Take input
n = int(input("Enter the number of rows: "))
print()

if n > 0:
    print(f"Half Pyramid Pattern ({n} rows):")
    print("-" * 30)
    
    # Outer loop to handle number of rows
    for i in range(n): 
        # Inner loop to handle number of columns
        for j in range(i + 1):
            # Display result with spacing
            print("* ", end="")
        print() # Move to the next line after each row
        
    print("-" * 30)
else:
    print("Please enter a positive number greater than 0.")

print()
print("====================================")
print("   Pattern generation complete!     ")
print("====================================")