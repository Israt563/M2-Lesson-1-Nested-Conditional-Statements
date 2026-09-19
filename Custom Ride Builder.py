# Custom Ride Builder
# File  : ride_builder.py
# Lesson: SPCM2L1 — Nested Conditional Statements (Jr)

print("====================================")
print("      Welcome to Ride Builder!      ")
print("====================================")
print()

print("Step 1: Pick your vehicle")
print("  1 - Bike")
print("  2 - Car")
print("  3 - Truck")
print()

choice = int(input("Enter 1, 2, or 3: "))
print()

# --- VEHICLE 1: BIKE ---
if choice == 1:
    print("Step 2: Pick your bike type")
    print("  1 - Scooty")
    print("  2 - Mountain Bike")
    print()

    bike_type = int(input("Enter 1 or 2: "))
    print()

    if bike_type == 1:
        print("You picked  : Scooty")
        print("Top speed   : 80 km/h")
        print("Best for    : City roads")
    elif bike_type == 2:
        print("You picked  : Mountain Bike")
        print("Top speed   : 40 km/h")
        print("Best for    : Off-road trails")
    else:
        print("Invalid bike type selected.")

# --- VEHICLE 2: CAR ---
elif choice == 2:
    print("Step 2: Pick your car type")
    print("  1 - Sedan")
    print("  2 - SUV")
    print()

    car_type = int(input("Enter 1 or 2: "))
    print()

    if car_type == 1:
        print("You picked  : Sedan")
        print("Seats       : 5 passengers")
        print("Best for    : Family trips")
    elif car_type == 2:
        print("You picked  : SUV")
        print("Seats       : 7 passengers")
        print("Best for    : Off-road adventures")
    else:
        print("Invalid car type selected.")

# --- VEHICLE 3: TRUCK (NEW!) ---
elif choice == 3:
    print("Step 2: Pick your truck type")
    print("  1 - Pickup Truck")
    print("  2 - Semi Truck")
    print()

    truck_type = int(input("Enter 1 or 2: "))
    print()

    if truck_type == 1:
        print("You picked  : Pickup Truck")
        print("Capacity    : Heavy hauling")
        print("Best for    : Transporting gear & towing")
    elif truck_type == 2:
        print("You picked  : Semi Truck")
        print("Capacity    : Massive cargo")
        print("Best for    : Long-distance freight delivery")
    else:
        print("Invalid truck type selected.")

# --- INVALID MAIN CHOICE ---
else:
    print("That was not a valid choice.")
    print("Please enter 1 for Bike, 2 for Car, or 3 for Truck.")

print()
print("====================================")
print("   Your custom ride is ready!       ")
print("   Enjoy the journey!               ")
print("====================================")