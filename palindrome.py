N = int(input("Enter a number: "))
a=str(N)
if a==a[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")