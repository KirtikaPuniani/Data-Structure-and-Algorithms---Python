#count digits in a number

import math
def countdigits(n):
    count = int(math.log10(n) + 1)
    return count

if __name__ == "__main__":
    n = 1258946
    digits = countdigits(n)
    print("Number of digits in n is:", digits)
    