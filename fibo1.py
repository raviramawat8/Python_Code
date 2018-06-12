num = int(input("Enter the no of terms"))
x = 0
y = 1
a = 0
while a < num:
    z = x + y
    x = y
    y = z
    a = a + 1
    print(z)
