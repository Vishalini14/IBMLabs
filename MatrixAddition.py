#1D Array Addition
# size=int(input("Enter size of array: "))
# X=[]
# Y=[]
# Z=[]
# for i in range(size):
#     X.append(int(input()))
# for i in range(size):
#     Y.append(int(input()))
#
# print("The first array: ",X)
# print("The second array: ",Y)
#
#
# for i in range(size):
#     Z.append(X[i]+Y[i])
# print("The Sum Array: ")
# print(Z)


#2D Array Addition

size=int(input("Enter the size of array: "))
A=[]
B=[]
C=[]

for i in range(size):
    for j in range(size):
        A.append(int(input()))
    B.append(A)
    A=[]
for i in range(size):
    for j in range(size):
        A.append(int(input()))
    C.append(A)
    A=[]
for i in range(size):
    for j in range(size):
        print(B[i][j]+C[i][j])