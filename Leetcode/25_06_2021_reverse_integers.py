class Solution:
    def reverse(self, x):
        if -2**31 < x < 2**31:
            rev = 0
            while x > 0:
                last_digit = x % 10
                x = x // 10
                rev = rev * 10 + last_digit
        else:
            return 0
        return rev
          
sol = Solution()
print(sol.reverse(321235))