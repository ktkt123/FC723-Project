# Class that uses the Euclidean Algorithm to find the gcd of two numbers
class EuclideanAlgorithm:

    # method to work the gcd of a and b
    def gcd(self, a, b):

        while b != 0:         # repeate until b becomes 0
            temp = b          # remember the current value of b
            b = a % b         # find the remainder
            a = temp          # move b into a

        return a     # return a which is the gcd


# test the class with fixed values
ea = EuclideanAlgorithm()
print("GCD of 360 and 19 is:", ea.gcd(360, 19))