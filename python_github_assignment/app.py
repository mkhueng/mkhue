# Greet the user when the program starts
print("Welcome to my Python program!")

# Ask the user for the number of hours they studied today
hours = input("How many hours did you study today? ")
hours = float(hours)

# Calculate the weekly study projection
weekly_hours = hours * 7

# Display the result to the user
print(f"You are on track to study {weekly_hours} hours this week.")

# Validate the input and stop the program if it's not a number
try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number.")
    exit()