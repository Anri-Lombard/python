def isPalindrome(x):
  rev = 0
  y = x
  while y > 0:
    last_digit = y % 10
    rev = rev * 10 + last_digit
    y = y // 10
  if rev != x:
    return False
  return True
  
print(isPalindrome(4244))
        