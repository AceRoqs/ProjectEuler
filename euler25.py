# Problem 25: 1000-digit Fibonacci number

def digitCount(num):
    digits = 0
    while num != 0:
        digits += 1
        num //= 10

    return digits

f = [1, 1]

while True:
    next = f[len(f) - 1] + f[len(f) - 2]
    f.append(next)
    if digitCount(next) == 1000:
        print(len(f))
        exit()
