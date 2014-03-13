# Problem 16: Power digit sum

def calcPower(base, power):
    num = base
    for x in range(1, power):
        num *= base
    return num

def sum_digits(num):
    sum = 0
    while num != 0:
        sum += num % 10
        num //=  10
    return sum

two_to_one_thousand = calcPower(2, 1000)  # 2**1000
print(sum_digits(two_to_one_thousand))