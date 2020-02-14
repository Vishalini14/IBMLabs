inpString=input("Enter a string: ")
inpString=inpString.casefold()
revString=reversed(inpString)
if list(inpString) == list(revString):
    print(f"{inpString.capitalize()} is a Palindrome.")
else:
    print(f"{inpString.capitalize()} is not a Palindrome.")