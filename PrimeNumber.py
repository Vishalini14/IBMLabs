inputnum = int(input("Enter any number: "))
if inputnum > 1:
    for i in range(2, inputnum):
        if(inputnum % i == 0):
            print(inputnum, "is not a prime number.")
            print(i, " times", inputnum//i, "is", inputnum)
            break
    else:
        print(inputnum, "is a prime number")
else:
    print(inputnum, "is not a prime number")