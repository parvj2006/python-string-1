# Input: Get the number from the user
number = int(input("Enter a number: "))

# Print the multiplication table
print(f"Multiplication table of {number}:")
for i in range(1, 11):  # Loop from 1 to 10
    print(f"{number} x {i} = {number * i}")
