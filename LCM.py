def calc_LCM(n1,n2):
    if n1>n2:
        greater = n1
    else:
        greater = n2
    while True:
        if (greater % n1 == 0) and (greater % n2 == 0):
            lcm = greater
            break
        greater += 1
    return lcm


num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
print("The LCM of ",num1," ",num2,"is ",calc_LCM(num1,num2))