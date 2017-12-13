import sys

# Check if argument was provided
digit_string = sys.argv[1]
my_sum = 0

for digit in digit_string:
    if digit.isdigit():
        my_sum += int(digit)
    else:
        print("Non-number found!")
        exit(1)

print(my_sum)
