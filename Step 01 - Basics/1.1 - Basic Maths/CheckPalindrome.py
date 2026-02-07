#pallindrome number
    
class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False

        original = x
        rev = 0

        while x > 0:
            lastdigit = x % 10
            x = x // 10
            rev = rev * 10 + lastdigit

        return original == rev

