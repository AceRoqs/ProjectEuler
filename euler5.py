# Problem 5: Smallest multiple
# The efficient solution uses prime factorizations.
# This solution is brute force and takes about a minute to compute.

num = 0
finished = False
while not finished:
    num += 2
    good = True
    for x in range(1, 21):
        if num % (21 - x) != 0:
            good = False
            break
    if good:
        finished = True

print(num)
