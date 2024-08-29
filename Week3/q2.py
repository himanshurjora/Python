n=int(input("enter "))
num = 1
for i in range(n):
    for j in range(num):
        print("*", end =" ")
    num += 1
    print("")

num1 = num-1
for i in range(num1):
    for j in range(num1-1):
        print("*", end =" ")
    num1 -= 1
    print("")
4
