# Problem 6: Sum square difference

def sumOfSquares(num):
    sum = 0
    for x in range(1, num + 1):
        sum += x * x

    return sum

def squareOfSums(num):
    sum = 0
    for x in range(1, num + 1):
        sum += x

    return sum * sum

sum_of_squares = sumOfSquares(100)
square_of_sums = squareOfSums(100)

print(square_of_sums - sum_of_squares)

