# Python program to check whether a number is an Armstrong number using a method
def checkArmstrong(num):
    temp = num
    digits = len(str(num))
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp = temp // 10

    return total == num
n = int(input("Enter a number: "))
if checkArmstrong(n):
    print(n, "is an Armstrong Number")
else:
    print(n, "is Not an Armstrong Number")