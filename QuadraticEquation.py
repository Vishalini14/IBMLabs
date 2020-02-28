# Solving quadratic equation : ax**2 + 5bx + 6c =0
import cmath

a = int(input("Enter the coefficient of x^2 "))
b = int(input("Enter the coefficient of x "))
c = int(input("Enter the coefficient of constant "))

# Formula used x = -b (+/-)sqrt((b**2) - (4*a*c)) / (2*a)

d = (b**2) - (4*a*c)

sol1 = (-b - cmath.sqrt(d)) / (2*a)
sol2 = (-b + cmath.sqrt(d)) / (2*a)

print("The solutions to the quadratic equation are {0} and {1}".format(sol1,sol2))