# Problem 14: Longest Collatz sequence

max_chain = 1
best_number = 1

for num in range(2, 1000000):
    x = num
    current_chain = 1
    while x != 1:
        if x % 2 == 0:
            x = x / 2;
        else:
            x = 3 * x + 1
        current_chain += 1

    if current_chain > max_chain:
        max_chain = current_chain
        best_number = num

print(best_number)
