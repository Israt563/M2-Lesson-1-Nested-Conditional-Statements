
print("====================================")
print("      Welcome to Sum Calculator!    ")
print("====================================")
print()

# Input an integer value 
n = int(input("Enter the number up to which you want to find the sum: "))
total_sum = 0
print()

# Iterates from 1 to n
for i in range(1, n + 1):
    total_sum += i  # Cleaner way to write total_sum = total_sum + i
    print(f"Adding {i} -> Current Sum: {total_sum}")

print()
print("====================================")
print(f" Final Sum from 1 to {n} is: {total_sum}")
print("====================================")