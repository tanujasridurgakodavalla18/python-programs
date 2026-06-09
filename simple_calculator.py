a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("1.Add 2.Sub 3.Mul 4.Div")
choice = int(input("Enter choice: "))

if choice == 1:
    print(a + b)
elif choice == 2:
    print(a - b)
elif choice == 3:
    print(a * b)
elif choice == 4:
    print(a / b)
else:
    print("Invalid choice")
