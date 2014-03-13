# Problem 7: 10001st prime

def isPrime(prime_list, num):
    for x in prime_list:
        if num % x == 0:
            return False
    return True

prime_list = [2]
num = 3
while len(prime_list) < 10001:
    if isPrime(prime_list, num):
        prime_list.append(num)
    num += 2

print(prime_list[10000])
