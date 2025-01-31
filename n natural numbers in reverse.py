# Input: Get the value of N from the user
N = int(input("Enter the value of N: "))

# Print natural numbers in reverse using a while loop
print(f"The first {N} natural numbers in reverse order:")
while N >= 1:  # Loop from N to 1 (inclusive)
    print(N, end=" ")
    N -= 1  # Decrement N by 1
