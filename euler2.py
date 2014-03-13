# Problem 2: Even Fibonacci numbers

sum = 0
term1 = 1
term2 = 2
while term2 < 4000000:
    if term2 % 2 == 0:
        sum += term2

    next_term = term1 + term2
    term1 = term2
    term2 = next_term

print(sum)
