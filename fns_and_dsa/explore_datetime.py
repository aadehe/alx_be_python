from datetime import datetime, timedelta


# Part 1: Display the Current Date and Time
def display_current_datetime():
    # Get the current date and time
    now = datetime.now()

    # Format the date and time in a readable way
    current_date = now.strftime("%Y-%m-%d %H:%M:%S")

    # Display the current date and time
    print(f"Current Date and Time: {current_date}")

# Part 2: Calculate a Future Date
# Calculate the future date by adding the specified number of days to the current date
def calculate_future_date(number_of_days):
    # Prompt the user to enter a number of days (as an integer).
    number_of_days = int(input("Enter the number of days: "))
    future_date = datetime.now() + timedelta(days=number_of_days)
    print(f"Future Date: {future_date.strftime('%Y-%m-%d')}")