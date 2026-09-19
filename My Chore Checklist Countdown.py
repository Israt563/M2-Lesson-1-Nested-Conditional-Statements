# My Chore Checklist Countdown
# File  : chore_checklist.py

print("====================================")
print("    Welcome to Chore Checklist!     ")
print("====================================")
print()

# PART 1: Set today's total number of chores (no list needed)
total_chores = 4
original_count = total_chores
print(f"You have {original_count} chores to finish today!\n")

# PART 2: Keep a counter for completed chores and the current chore number
completed_count = 0
chore_num = 1

# PART 3: Repeat while there are still chores left to check off
while chore_num <= total_chores:

    # PART 4: Work out the current chore's name from its number
    if chore_num == 1: 
        next_chore = "Make your bed"
    elif chore_num == 2: 
        next_chore = "Feed the pet"
    elif chore_num == 3: 
        next_chore = "Take out the trash"
    else: 
        next_chore = "Wash the dishes"

    # Using .strip().lower() makes user input more forgiving of typos or capitalization
    answer = input(f"Have you finished: {next_chore}? (yes/no): ").strip().lower()
    print()

    # PART 5: Only move on to the next chore once it is marked done
    if answer == "yes" or answer == "y":
        completed_count += 1
        chore_num += 1
        print("Great job! Chore completed 🎉")
    else:
        print("Okay, finish it and check again! ⏳")

    # PART 6: Print how many chores remain after each check
    print(f"Chores remaining: {total_chores - completed_count}")
    print("-" * 36)
    print()

# PART 7: This only prints once every chore is marked done
print("===== ALL CHORES COMPLETE! =====")
print("Great work finishing your entire checklist today!\n")

# PART 8: A safe look at what an infinite loop would look like
print("Now let's safely peek at an infinite loop...")
test_value = 0
safety_counter = 0
while test_value <= 0:
    print("This condition never changes, so this would run forever!")
    safety_counter += 1
    if safety_counter == 3:
        print("(Stopping here on purpose - a real infinite loop never stops on its own!)")
        break

# PART 9: Print the final chore checklist summary
print("\n===== CHORE CHECKLIST SUMMARY =====")
print(f"Chores Assigned Today : {original_count}")
print(f"Chores Completed      : {completed_count}")
print(f"Chores Remaining      : {total_chores - completed_count}")
print("======================================")