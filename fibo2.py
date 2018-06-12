num = int(input("Enter the no of terms"))
x = int(input("Enter the First no."))
y = int(input("Enter the Second no."))
a = 0
while a < num:
    z = x + y
    x = y
    y = z
    a += 1
    print(z)
