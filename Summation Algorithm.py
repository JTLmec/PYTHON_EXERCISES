# Top 5 sectors with the highest number of employed persons in Data for November 2024
nov_2024_data = {
    "Wholesale and retail trade; repair of motor vehicles and motorcycles": 746000,
    "Accommodation and food service activities": 389000,
    "Other service activities": 328000,
    "Manufacturing": 231000,
    "Transportation and storage": 113000
}

# top 5 sectors with the highest number of employed persons in Data for February 2025
feb_2025_data = {
    "Accommodation and food service activities": 377000,
    "Fishing and aquaculture": 365000,
    "Public administration and defense; compulsory social security": 330000,
    "Construction": 258000,
    "Other service activities": 232000
}

# Summation algorithm to calculate total number of employed persons
def calculate_total(data):
    total = 0
    for sector, employed in data.items():
        total += employed
    return total

# Calculate total number of employed persons for November 2024
nov_2024_total = calculate_total(nov_2024_data)
print(f"Total number of employed persons in the top 5 sector for November 2024: {nov_2024_total} thousand")

# Calculate total number of employed persons for February 2025
feb_2025_total = calculate_total(feb_2025_data)
print(f"Total number of employed persons in in the top 5 sector for February 2025: {feb_2025_total} thousand")

# Calculate percentage change in total number of employed persons
percentage_change = ((feb_2025_total - nov_2024_total) / nov_2024_total) * 100
print(f"Percentage change in total number of employed persons: {percentage_change:.2f}%")