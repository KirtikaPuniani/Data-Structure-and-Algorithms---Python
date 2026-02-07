#GCD of 2 numbers

def findGCD(n1, n2):
    gcd = 1
    
    for x in range(1, min(n1, n2)+1):
        if n1 % x == 0 and n2 % x == 0:
            gcd = x
    return gcd

if __name__ == "__main__":
    # n1, n2 = 15, 3
    gcd = findGCD(n1, n2)
    print("GCD of", n1, "and", n2, "is:", gcd)
    
a = findGCD(15, 3)
b = findGCD(50, 65)
print(a)
print(b)


# Time Complexity: O(min(N1, N2)) where N1 and N2 is the input number. The algorithm iterates from 1 to the minimum of N1 and N2 and 
# each iteration checks whether both the numbers are divisible by the current number (constant time operations).

# Space Complexity: O(1)as the space complexity remains constant and independent of the input size. Only a fixed amount of memory is 
# required to store the integer variables.

#-----------------------------------------------------------------------------------------------------------------------------------#

#optimal solution


def find_gcd(a, b):
    # Continue loop as long as both
    # a and b are greater than 0
    while a > 0 and b > 0:
        # If a is greater than b,
        # subtract b from a and update a
        if a > b:
            # Update a to the remainder
            # of a divided by b
            a = a % b
        # If b is greater than or equal
        # to a, subtract a from b and update b
        else:
            # Update b to the remainder
            # of b divided by a
            b = b % a
    # Check if a becomes 0,
    # if so, return b as the GCD
    if a == 0:
        return b
    # If a is not 0,
    # return a as the GCD
    return a


def main():
    n1 = 20
    n2 = 15

    # Find the GCD of n1 and n2
    gcd = find_gcd(n1, n2)

    print(f"GCD of {n1} and {n2} is: {gcd}")


if __name__ == "__main__":
    main()
    
    
# Time Complexity: O(min(N1, N2)) where N1 and N2 is the input number. The algorithm iterates from the minimum of N1 and N2 to 1 and 
# each iteration checks whether both the numbers are divisible by the current number (constant time operations).

# Space Complexity: O(1) as the space complexity remains constant and independent of the input size. Only a fixed amount of memory is 
# required to store the integer variable