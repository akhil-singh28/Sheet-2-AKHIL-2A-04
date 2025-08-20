N = int(input("Enter a number: "))
original = N
reversed_num = 0
while N > 0:
    digit = N % 10
    reversed_num = reversed_num * 10 + digit
    N //= 10
if original == reversed_num:
    print("Palindrome")
else:
    print("Not a palindrome")