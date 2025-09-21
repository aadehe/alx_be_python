# Prompt for a Single Task
task = input("Enter a task: ")

# prompt for priority level
priority = input("Priority (high, medium, low): ").lower()

# Prompt for time bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the Task Based on Priority and Time Sensitivity
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
    case "low":
        if time_bound == "no":
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print(f"Reminder: '{task}' is a {priority} priority task. Plan accordingly!")
