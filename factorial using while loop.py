# Function to calculate factorial using a while loop
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        i = 2
        while i <= n:  # Loop from 2 to n
            result *= i
            i += 1
        return result

# Input: Get the number from the user
number = int(input("Enter a number: "))

# Calculate and print the factorial
print(f"The factorial of {number} is: {factorial(number)}")
