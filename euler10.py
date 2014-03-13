# Problem 10: Summation of primes

sum = 0

# Calculate sieve of Eratosthenes.
prime_list = [True for x in range(2000000)]
prime_list[0] = prime_list[1] = False
num = 2
while num < len(prime_list):
    if prime_list[num]:
        x = num + num
        while x < len(prime_list):
            prime_list[x] = False
            x += num
        sum += num
    num += 1

print(sum)
