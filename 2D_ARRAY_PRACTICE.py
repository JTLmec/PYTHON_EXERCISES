# 2D array representing bus schedules 
bus_schedules = [
    ["05:00", "06:00", "07:00", "08:00", "09:00", "10:00", "11:00", "12:00"],
    ["13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00"],
    ["21:00", "22:00", "23:00"]
]

# Function to append a time and automatically sort the bus schedule
def append_and_sort(bus_index, time):
    if time not in bus_schedules[bus_index]:
        bus_schedules[bus_index].append(time)
        bus_schedules[bus_index].sort()
        print(f"{time} added to Bus Schedule {bus_index +1}.")
    else:
        print(f"{time} is already in Bus Schedule {bus_index + 1}.")

# Function to remove a time and automatically sort the bus schedule
def remove_and_sort(bus_index, time):
    if time in bus_schedules[bus_index]:
        bus_schedules[bus_index].remove(time)
        bus_schedules[bus_index].sort()
        print(f"{time} removed from Bus Schedule {bus_index + 1}.")
    else:
        print(f"{time} not found in the schedule.")

# Function to search for a specific time in a bus schedule
def search_time(bus_index, time):
    if time in bus_schedules[bus_index]:
        print(f"{time} found in Bus Schedule {bus_index + 1}.")
    else:
        print(f"{time} not found in Bus Schedule {bus_index + 1}.")

# Function to display all bus schedules
def display_schedules():
    print("\nBus Schedules:")
    for i, row in enumerate(bus_schedules):
        print(f"Bus Schedule {i + 1}: {', '.join(row)}")

# Checking if added bus time is valid
def check_valid_time(time):
    digits = time.split(":")
    if len(digits) != 2:
        return False
    try:
        hour = int(digits[0])
        minutes = int(digits[1])
        return 0<= hour < 24 and 0 <= minutes < 60
    except ValueError:
        return False

# Menu-driven interface
def bus_schedule_app():
    while True:
        print("\nBus Schedule Management System")
        print("1. Add a bus time")
        print("2. Remove a bus time")
        print("3. Search for a bus time")
        print("4. Display all schedules")
        print("5. Exit")

        # Get user choice
        choice = input("Enter your choice (1-5): ")
        
        if choice in {"1","2","3"}:
            try:
                bus_index = int(input("Enter bus schedule number (1-3): ")) - 1
                if bus_index not in range(3):
                    print("Invalid bus schedule number. Please enter 1, 2, or 3.")
                    continue
                time = input("Enter the time (HH:MM format): ")
                if not check_valid_time(time):
                    print("Invalid time format. Please enter in HH:MM format (e.g. 14:30).")
                    continue
                if choice == "1":
                    # Add a bus time
                    append_and_sort(bus_index, time)
                elif choice == "2":
                    # Remove a bus time
                    remove_and_sort(bus_index,time)
                elif choice == "3":
                    # Search for a bus time
                    search_time(bus_index, time)
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 3.")
        elif choice == "4":
            # Display all schedules
            display_schedules()
        elif choice == "5":
            # Exit the app
            print("Exiting the Bus Schedule Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Run the app
bus_schedule_app()
