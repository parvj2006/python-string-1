# Function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Function to calculate nCr (combinations)
def nCr(n, r):
    if r > n:
        return 0  # Invalid case
    return factorial(n) // (factorial(r) * factorial(n - r))

# Function to calculate nPr (permutations)
def nPr(n, r):
    if r > n:
        return 0  # Invalid case
    return factorial(n) // factorial(n - r)

# Input: Get values of n and r from the user
n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))

# Calculate and print nCr and nPr
print(f"{n}C{r} (Combinations) = {nCr(n, r)}")
print(f"{n}P{r} (Permutations) = {nPr(n, r)}")
