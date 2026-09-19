# Floyd's Triangle Generator
# File  : floyds_triangle.py

print("====================================")
print("    Welcome to Floyd's Triangle!    ")
print("====================================")
print()

# Take input from user
rows = int(input("Please enter the total number of rows: "))
print()

if rows > 0:
    number = 1  # Initialize by 1
    print(f"Floyd's Triangle ({rows} rows):")
    print("-" * 30)
    
    # Outer loop for number of rows
    for i in range(1, rows + 1):
        # Inner loop for number of columns
        for j in range(1, i + 1):     
            # Display result with fixed width spacing for neat alignment
            print(f"{number:<3}", end='')
            number += 1
        print()
        
    print("-" * 30)
else:
    print("Please enter a positive number greater than 0.")

print()
print("====================================")
print("   Triangle generation complete! 📐 ")
print("====================================")