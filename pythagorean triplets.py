# Define the maximum side length
max_side = 30

# Generate all Pythagorean triplets
print("Pythagorean Triplets with sides <= 30:")
for a in range(1, max_side + 1):
    for b in range(a, max_side + 1):  # Start from a to avoid duplicate triplets
        for c in range(b, max_side + 1):  # Start from b to avoid duplicate triplets
            if a**2 + b**2 == c**2:  # Check Pythagorean theorem
                print(f"({a}, {b}, {c})")
