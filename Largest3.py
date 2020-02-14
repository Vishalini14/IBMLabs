n1=input("Enter first number: ")
n2=input("Enter second number: ")
n3=input("Enter third number: ")

if(n1>=n2) and (n1>=n3):
    large=n1
elif (n2>=n1) and (n2>=n3):
    large=n2
else:
    large=n3
print("Largest number",large)