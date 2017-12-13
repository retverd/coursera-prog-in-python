import decimal
import sys
from decimal import Decimal

# Check if arguments were provided
# Ensure definition of a, b & c
a_str = sys.argv[1]
b_str = sys.argv[2]
c_str = sys.argv[3]

try:
    a = Decimal(a_str)
except decimal.InvalidOperation:
    print("First argument is not decimal!")
    exit(1)

if a == 0:
    print("This isn't quadratic equation!")
    exit(2)

try:
    b = Decimal(b_str)
except decimal.InvalidOperation:
    print("Second argument is not decimal!")
    exit(1)

try:
    c = Decimal(c_str)
except decimal.InvalidOperation:
    print("Third argument is not decimal!")
    exit(1)

D = Decimal(b ** 2 - 4 * a * c)

if D < 0:
    print("There are no real roots")
elif D == 0:
    print((-b / (2 * a)).normalize())
else:
    print(((-b + D ** Decimal(0.5)) / (2 * a)).normalize())
    print(((-b - D ** Decimal(0.5)) / (2 * a)).normalize())
