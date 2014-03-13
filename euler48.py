# Problem 48: Self powers

def lastDigits(num, count):
    return int(str(num)[-count:])

sum = 0
for x in range(1, 1000):
    sum += x**x

print(lastDigits(sum, 10))