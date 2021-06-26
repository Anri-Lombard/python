

class Solution:
    def reverse(self, x):
        if -2**31-1 < x < 2**31-1:
            sign = 1 # Make sure negative ends up negative
            if x < 0:
                sign = -1
                x *= -1
            rev = 0
            while x != 0:
                last_digit = x % 10
                x = x // 10
                rev = rev * 10 + last_digit
        else:
            return 0
        return sign * rev
          
sol = Solution()
print(sol.reverse(-123))