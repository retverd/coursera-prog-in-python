import sys

# Check if argument was provided
# Ensure definition of num_stairs
digit_string = sys.argv[1]

if digit_string.isdigit():
    num_stairs = int(digit_string)
else:
    print("Natural number is expected!")
    exit(1)

for i in range(num_stairs):
    print(" " * (num_stairs - (i + 1)) + "#" * (i + 1))
