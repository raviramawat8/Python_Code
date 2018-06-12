x = int(input("Enter the Starting point"))
y = int(input("Enter the Ending point "))
i=2
while x<y:
    while i<x:
        if x % i == 0:
            break
        else:
            print(x)
        i = i + 1
    x += 1
