# Input: Get the string from the user
input_string = input("Enter a string: ")

# Initialize counters
alphabet_count = 0
digit_count = 0

# Loop through each character in the string
for char in input_string:
    if char.isalpha():  # Check if the character is an alphabet
        alphabet_count += 1
    elif char.isdigit():  # Check if the character is a digit
        digit_count += 1

# Output the results
print(f"Number of alphabets: {alphabet_count}")
print(f"Number of digits: {digit_count}")
