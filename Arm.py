x = int(input("Enter a number"))
n = x
sum = 0
while n > 0:
    a = n % 10
    sum += a ** 3
    n //= 10
if x == sum:
    print("The Number is Armstrong no.")
else:
    print("Not Armstrong")
