A = int(input("Enter the value of A: "))
total = 0
for i in range(1, A + 1):
    if i % 2 == 0:
        total += i
print(total)