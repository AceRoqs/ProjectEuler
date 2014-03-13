# Problem 9: Special Pythagorean triplet

for a in range(1001):
    for b in range(a + 1, 1001):
        for c in range(b + 1, 1001):
            if a + b + c == 1000:
                if a*a + b*b == c*c:
                    print(a*b*c)
                    exit()
