a1 = int(input("Enter a number"))
num = a1
count = 0
res = 0
x=0
while a1 > 0:
    x = a1 % 10
    res = res*10 + x
    a1 = a1 // 10
    count += 1
if num == res:
    print("This no. is Palindrome")
else:
    print("Not a Palindrome")
print("Length = {}".format(count))

