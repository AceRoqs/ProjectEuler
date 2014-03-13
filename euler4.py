# Problem 4: Largest palindrome product

def isPalindrome(num):
    reverse = 0
    x = num
    while x > 0:
        reverse *= 10
        reverse += x % 10
        x //= 10
    if num == reverse:
        return True
    else:
        return False

x = 0
y = 0
max_palindrome = 0
for x in range(100, 1000):
    for y in range(100, 1000):
        product = x * y
        if product > max_palindrome:
            if isPalindrome(product):
                max_palindrome = product

print(max_palindrome)
