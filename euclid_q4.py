# Euclidean Algorithm class with keyboard input

class EuclideanAlgorithm:

    # method to work the gcd of a and b
    def gcd(self, a, b):
        while b != 0:       # repeate until b becomes 0
            temp = b        # remember the current value of b
            b = a % b       # find the remainder
            a = temp        # move b into a
        return a


# get first number
first = input("Enter the first positive integer: ")

# get second number
second = input("Enter the second positive integer: ")

# Check both inputs are only numbers
if not first.isdigit() or not second.isdigit():
    print("Error: please enter positive integers only.")
else:
    # convert to integers
    a = int(first)
    b = int(second)

    # Check both numbers are greater than zero
    if a <= 0 or b <= 0:
        print("Error: both numbers must be greater than zero.")
    else:
        ea = EuclideanAlgorithm()
        gcd_value = ea.gcd(a, b)
        print(f"The GCD of {a} and {b} is {gcd_value}")