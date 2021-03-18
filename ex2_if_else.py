# def calculetor():
#     print("\nWellcome to Calc: This is Developed by Subham Roy")
#     operation = input('''
#     Please type in the math operation you would like to complete:
#     + for addition
#     - for subtraction
#     * for multiplication
#     / for division
#     ** for power
#     % for modulo
#
#     Enter Your Choise:
#     ''')
#
#     num1 = int(input("Enter first Number: "))
#     num2 = int(input("Enter second Number: "))
#
#     if operation == '+':
#         if num1 == 56:
#             print("56 + 9 = 77")
#         else:
#             print(f"{num1} + {num2} = {num1 + num2}")
#     elif operation == '-':
#         print(f"{num1} - {num2} = {num1 - num2}")
#     elif operation == '*':
#         if num1 == 45:
#             print("45 * 3 = 555")
#         else:
#             print(f"{num1} * {num2} = {num1 * num2}")
#     elif operation == '/':
#         if num1 == 56:
#             print("56/6 = 4")
#         else:
#             print(f"{num1} / {num2} = {num1 / num2}")
#     elif operation == '**':
#         print(f"{num1} ** {num2} = {num1 ** num2}")
#     elif operation == '%':
#         print(f"{num1} % {num2} = {num1 % num2}")
#     else:
#         print("You Press a Invalid Key")
#     again()
#
#
# def again():
#     cal_again = input('''
#     Do you want to calculate again?
#     Please type y for YES or n for NO.
#     ''')
#
#     if cal_again == 'y':
#         calculetor()
#     elif cal_again == 'n':
#         print("See You Later")
#     else:
#         again()
#
#
# calculetor()

def calculetor():
   print("\nWelcome to Mrinmoy Basak Calculator")
   num1 = int(input("Please enter 1st Number: "))
   num2 =  int(input("Please enter 2nd Number: "))
   opp= input("please enter +,-,*,/:- \n")

   if opp == '+':
        if num1 == 56 and num2 == 9:
            print("56 + 9 = 77")
        elif num1 == 9 and num2 == 56:
            print("9 + 56 = 77")
        else:
            print(f"{num1} + {num2} = {num1 + num2}")
   elif opp == '*':
       if num1 == 45 and num2 == 3:
           print("45*3 = 555")
       elif num1 == 3 and num2 == 45:
           print("3*45=555")
       else:
           print(f"{num1} * {num2} = {num1 * num2}")

   elif opp == '-':
        print(f"{num1} - {num2} = {num1 - num2}")
   elif opp == '/':
    if num1 == 56 and num2 == 6:
        print("56/6 = 4")
    elif num1 == 6 and num2 == 56:
        print("6/56= 4")
    else:
        print(f"{num1} / {num2} = {num1 / num2}")


   else:
     print("You Press a Invalid Key")
   again()



def again():
    cal_again = input('''
    Do you want to calculate again?
    Please type y for YES or n for NO.
    ''')

    if cal_again == 'y':
        calculetor()
    elif cal_again == 'n':
        print("See You Later")
    else:
        again()




calculetor()
