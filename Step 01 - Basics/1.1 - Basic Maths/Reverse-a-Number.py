#reverse a number

class Solution(object):
    def reverse(self, x):
        rev = 0
        
        while x>0:
            lastdigit = x % 10
            rev = rev * 10 + lastdigit
            x = x//10
        
        return rev
    
X = Solution()
print(X.reverse(7789))
        
        
# class Solution(object):
#     def reverse(self, x):
#         rev = 0

#         while x > 0:
#             lastdigit = x % 10
#             rev = rev * 10 + lastdigit
#             x = x // 10

#         return rev

# X = Solution()
# print(X.reverse(7789))
