# def dec1():
#     print("mrinmoy")
#
# v=dec1
# del dec1
# v()

# def funcret(num):
#     if num == 0:
#         return ("mrinmoy")
#     if num == 1:
#         return ("manika")
#
# a = funcret(1)
# print(a)

# def executor(func):
#     func("Mrinmoy")
# executor(print)

# def dec1(func1):
#     def nowexec():
#         print("Executing Now")
#         func1()
#         print("Executed")
#     return nowexec
# @dec1
# def who_is_mrinmoy():
#     print("Mrinmoy is a good boy")
# # who_is_mrinmoy = dec1(who_is_mrinmoy)
# who_is_mrinmoy()


def mathsum(a,b):
    return (a+b)


def mathmul(a,b):
    return (a*b)


def again():
    num1 = int(input())
    num2 = int(input())
    com1 = str(input())

    cal1 = mathsum(num1,num2)
    cal2 = mathmul(num1,num2)

    while True:
        if(com1== "s"):
            print(cal1)
            break
        elif(com1=="m"):
            print(cal2)
            break
        else:
            print("please enter valid input")
            break






again()



