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


#############################
#          EXAMPLES         #
#############################
               
# Example: Append "XX:XX" to the first bus schedule and sort
append_and_sort(0, "08:30")
# Example: Remove "XX:XX" from the first bus schedule and sort
remove_and_sort(0, "08:00")

# Example: Append "XX:XX" to the second bus schedule and sort
append_and_sort(1, "14:30")
# Example: Remove "XX:XX" from the second bus schedule and sort
remove_and_sort(1, "15:00")

# Example: Append "XX:XX" to the third bus schedule and sort
append_and_sort(1, "22:30")
# Example: Remove "XX:XX" from the third bus schedule and sort
remove_and_sort(1, "22:00")

# Example: Search for "XX:XX" in the first bus schedule
search_time(0, "08:30")  # Output: "XX:XX found in bus schedule 1."

# Example: Search for "XX:XX" in the second bus schedule
search_time(1, "15:30")  # Output: "XX:XX not found in bus schedule 2."

# Example: Search for "XX:XX" in the second bus schedule
search_time(1, "22:30")  # Output: "XX:XX not found in bus schedule 3."

# Function to print all bus schedules in column format
print("\nBus Schedules:")
for row in bus_schedules:
    for column in row:
        print(column)
