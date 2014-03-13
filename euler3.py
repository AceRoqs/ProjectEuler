# Problem 3: Largest prime factor

def isPrime(prime_list, num):
    for x in prime_list:
        if num % x == 0:
            return False
    return True

def allFactors(factors, target):
    num = 1
    for x in factors:
        num *= x

    if num == target:
        return True
    return False

prime_list = [2]
factors = []
num = 3
target = 600851475143

while True:
    if isPrime(prime_list, num):
        prime_list.append(num)
        if target % num == 0:
            factors.append(num)
            if allFactors(factors, target):
                print(factors[len(factors) - 1])
                exit()
    num += 2
