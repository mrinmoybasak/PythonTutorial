# i=0
# while(True):
#     print(i+1, end=" ")
#     if (i==44):
#         break
#
#     i = i+1
#


# i=0
# while(True):
#     if i+1<10:
#         i= i+1
#         continue
#
#
#     print(i+1, end=" ")
#     if (i==44):
#         break
#
#     i = i+1

while(True):
    inp = int(input("Please enter the number\n"))
    if inp>100:
        print("Contraz you are enter 100 above number")
        break
    else:
        print("please try again\n")
        continue
