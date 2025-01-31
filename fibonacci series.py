# Input: Get the value of N from the user
N = int(input("Enter the value of N: "))

# Initialize the first two Fibonacci numbers
a, b = 0, 1

# Print the first N Fibonacci numbers
print(f"The first {N} Fibonacci numbers are:")
for _ in range(N):
    print(a, end=" ")
    a, b = b, a + b  # Update the values of a and b
