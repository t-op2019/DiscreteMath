def gcd(a, b):
    if a > b:
        return gcd(b, a)
    if a == 0:
        return b
    if (a % 2 == 0) & (b % 2 == 0):
        return 2 * gcd(a / 2, b / 2)
    elif a % 2 == 0:
        return gcd(a / 2, b)
    else:
        return gcd(a, b - a)


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Greatest common divisor of", a, "and", b, "is", int(gcd(a, b)))
