num1 = int(input("enter "))

for i in range(num1):
    num = num1
    for j in range(num1):
        print(num, end =" ")
        num -= 1
    num1 -= 1
    print("")
