# pattern_drawing.py

# Ask the user to enter the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop to print each row
while row < size:
    # Use a for loop to print '*' in one row
    for _ in range(size):
        print("*", end="")
    print()  # Move to the next line after one row
    row += 1
