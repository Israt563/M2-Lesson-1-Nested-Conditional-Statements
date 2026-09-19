# Number Diamond Pattern Generator
# File  : number_diamond.py

print("====================================")
print("    Welcome to Number Diamond!      ")
print("====================================")
print()

# Take input from user
rowSize = int(input("Enter the number of rows (odd numbers work best): "))
print()

if rowSize > 0:
    if rowSize % 2 == 0:  # conditions
        halfDiamRow = int(rowSize / 2)
    else:
        halfDiamRow = int(rowSize / 2) + 1
        
    space = halfDiamRow - 1
    
    print(f"Number Diamond Pattern ({rowSize} rows):")
    print("-" * 35)
    
    # Loop for upper part 
    for i in range(1, halfDiamRow + 1):  # loop for rows
        for j in range(1, space + 1):  # loop for columns
            print(end=" ")
        space = space - 1
        num = 1
        for j in range(2 * i - 1):
            print(end=str(num))
            # Incrementing number at each column
            num = num + 1
        print()
        
    space = 1
    # Loop for lower part
    for i in range(1, halfDiamRow):  # loop for rows
        for j in range(1, space + 1):   # loop for columns
            print(end=" ")
        space = space + 1
        num = 1
        for j in range(1, 2 * (halfDiamRow - i)):
            print(end=str(num))  # display result
            # Incrementing number at each column
            num = num + 1
        print()
        
    print("-" * 35)
else:
    print("Please enter a positive number greater than 0.")

print()
print("====================================")
print("   Diamond generation complete! 💎  ")
print("====================================")