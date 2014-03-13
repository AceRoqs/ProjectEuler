# Problem 36: Double-base palindromes

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

def isBinaryPalindrome(num):
    num1 = num
    num2 = 0
    while num != 0:
        num2 *= 2
        if num % 2 != 0:
            num2 += 1
        num //= 2

    return num1 == num2

sum = 0
for x in range(1, 1000000):
    if isPalindrome(x):
        if isBinaryPalindrome(x):
            sum += x

print(sum)