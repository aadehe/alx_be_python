# Prompt User for Pattern Size
size = int(input("Enter the size of the pattern: "))

# Draw the Pattern
counter = size
while counter != 0:
    for i in range(size):
        print("*", end="")
    print()
    counter -= 1


