num1 = input("Enter 1st number: ")
num2 = input("Enter 2nd number: ")

try:
    print("the sum of two number", int(num1)+int(num2))

except Exception as e:
    print(e)

print("This line is very important")