# Scratch pad for trying some approaches to Project Euler problems.

def isPalindrome(i):
    j = 0
    x = i
    while x > 0:
        j *= 10
        j += x % 10
        x //= 10
    if i == j:
        return True
    else:
        return False


def isPalindrome2(i):
    j = 0
    x = i
    while x > 0:
        j *= 2
        j += x % 2
        x //= 2
    if i == j:
        return True
    else:
        return False


def sumOfDigits(a):
    sum = 0
    while a > 0:
        sum += a % 10
        a //= 10
    return sum


def factorial(a):
    if a == 1:
        return 1
    return a * factorial(a-1)

def expn2(a):
    z = 1
    for x in range(a):
        z *= 2
    return z

def expnN(a,N):
    z = 1
    for x in range(a):
        z *= N
    return z


def sexp(x):
    sum = 0
    for a in range(x):
        sum += expnN(a, a)
    print(sum)

print(sumOfDigits(factorial(100)))
sum = 0
for a in range(1000000):
    if isPalindrome(a) and isPalindrome2(a):
        sum += a



max = 0
for a in range(1000):
    for b in range(1000):
        next = a*b
        if isPalindrome(next):
            if next > max:
                max = next

a = [y for y in range(3,2000000,2)]

for b in a:
    for c in a:
        if b != c:
            if c % b == 0:
                a.remove(c)

a = [y for y in range(3,200000,2)]
a.insert(0, 2)
ix = 1
while ix < len(a):
    b = []
    #print("Removing multiples of ", a[ix], len(a))
    for ix2 in range(ix, len(a)):
        if a[ix2] != a[ix]:
            if a[ix2] % a[ix] == 0:
                #print("Removing ", a[ix2])
                b.append(a[ix2])
    for c in b:
        a.remove(c)
    ix+=1

print(sumlist(a))

def sumlist(x):
    sum = 0
    for a in x:
        sum += a
    return sum


a = [True for y in range(200000)]
a[0] = False
a[1] = False
ix = 2
while ix < len(a):
    #print("Removing multiples of ", a[ix], len(a))
    for ix2 in range(ix, len(a)):
        if ix2 != ix:
            if ix2 % ix == 0:
                #print("Removing ", a[ix2])
                a[ix2] = False
    ix+=1

def nextnumber(x):
    if x%2 == 0:
        return x//2
    return 3*x+1


def getseq(x):
    a=[x]
    while x != 1:
        x = nextnumber(x)
        a.append(x)
    return a


def getmax():
    b = 1
    num = 1
    for i in range(2,1000000):
        a = getseq(i)
        #print(i)
        if len(a) > b:
            b = len(a)
            num = i
    print(num)

a=1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
f1=1
f2=1
fnext = f1+f2
x=3
while fnext < a:
    f1=f2
    f2=fnext
    fnext = f1+f2
    x += 1

print(x)
