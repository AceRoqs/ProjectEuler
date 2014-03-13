# Problem 20: Factorial digit sum

def factorial(num):
    sum = 1
    while num != 0:
        sum *= num
        num -= 1
    return sum

def sum_digits(num):
    sum = 0
    while num != 0:
        sum += num % 10
        num //=  10
    return sum

print(sum_digits(factorial(100)))