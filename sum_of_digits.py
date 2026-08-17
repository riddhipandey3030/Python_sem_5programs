# Python program to find the sum of digits using a method
def doSum(num):
    total = 0
    while num > 0:
        digit = num % 10
        total += digit
        num = num // 10
    return total
n = int(input("Enter a number: "))
result = doSum(n)
print("Sum of digits =", result)