class Calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def sum(self):
        return f"Your Total number is {self.num1+self.num2}"

    def subtraction(self):
        return f"Your Subtract is {self.num1 - self.num2}"

    def multiply(self):
        return f"Your Multilpy number is {self.num1 * self.num2}"

    def division(self):
        return f"Your Division number is {self.num1/self.num2}"




inp1 = int(input("Enter 1st No\n"))
inp2 = int(input("Enter 2nd Number\n"))
print("What you want to do type p for Sum , type s for Subtract , type m for Multiply , type d for Division\n ")
cal1= Calculator(inp1,inp2)
met = input()
if met == 'p' :
    print(cal1.sum())
elif met == 's':
    print(cal1.subtraction())
elif met == 'm':
    print(cal1.multiply())
elif met == 'd':
    print(cal1.division())
else:
    print("Please Enter a valid input")















