a = float(input("Enter First Number : "))
b = float(input("Enter second number : "))

m = int(input("Enter mod number : "))
# a = int(a) if isinstance(a, int) else float(a)
# b = int(b) if isinstance(b, int) else float(b)

print(type(a ** b))
rem = a**b%m
print(a**b%m)