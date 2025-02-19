# 2D array representing bus schedules
bus_schedules = [
    ["05:00", "06:00", "07:00", "08:00", "09:00", "10:00", "11:00", "12:00"],
    ["13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00"],
    ["21:00", "22:00", "23:00"]
]

# Function to append a time and automatically sort the bus schedule
def append_and_sort(bus_index, time):
    bus_schedules[bus_index].append(time)
    bus_schedules[bus_index].sort()

# Function to remove a time and automatically sort the bus schedule
def remove_and_sort(bus_index, time):
    if time in bus_schedules[bus_index]:
        bus_schedules[bus_index].remove(time)
        bus_schedules[bus_index].sort()
    else:
        print(f"{time} not found in the schedule.")

# Function to search for a specific time in a bus schedule
def search_time(bus_index, time):
    if time in bus_schedules[bus_index]:
        print(f"{time} found in bus schedule {bus_index + 1}.")
    else:
        print(f"{time} not found in bus schedule {bus_index + 1}.")

# Function to display all bus schedules
def display_schedules():
    print("\nBus Schedules:")
    for i, row in enumerate(bus_schedules):
        print(f"Bus Schedule {i + 1}: {', '.join(row)}")

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

        if choice == "1":
            # Add a bus time
            bus_index = int(input("Enter bus schedule number (1-3): ")) - 1
            time = input("Enter the time to add (HH:MM format): ")
            append_and_sort(bus_index, time)
            print(f"Time {time} added to bus schedule {bus_index + 1}.")
        elif choice == "2":
            # Remove a bus time
            bus_index = int(input("Enter bus schedule number (1-3): ")) - 1
            time = input("Enter the time to remove (HH:MM format): ")
            remove_and_sort(bus_index, time)
        elif choice == "3":
            # Search for a bus time
            bus_index = int(input("Enter bus schedule number (1-3): ")) - 1
            time = input("Enter the time to search for (HH:MM format): ")
            search_time(bus_index, time)
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
