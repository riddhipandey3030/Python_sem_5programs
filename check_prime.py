# Python program to check whether a number is prime or not using a method
def isprime(num):
    if num <= 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True
n = int(input("Enter a number: "))
if isprime(n):
    print(n, "is a Prime Number")
else:
    print(n, "is Not a Prime Number")