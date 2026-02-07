class AllDivisors(object):
    def divisors(self, n):
        for x in range(1, n+1):
            if n % x == 0:
                print(x)

obj = AllDivisors()
obj.divisors(36)

#Time Complexity : O(n)
#Space Complexity : O(1)

###################################################################

'''More Optimised Soln'''

class AllDivisors(object):
    def divisors(self, n):
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                print(i)
                if i != n // i:
                    print(n // i)

#Time Complexity : O(√n)
#Space Complexity : O(1)

'''O(√n) is better than O(n) because the number of operations grows much slower, and divisor pairs allow us to stop at the square root.'''