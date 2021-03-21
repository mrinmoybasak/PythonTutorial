#
# print("How Many Row You Want To Print")
# one= int(input())
# print("Type 1 Or 0")
# two = int(input())
# new =bool(two)
# if new == True:
#     for i in range(1,one+1):
#         for z in range(1,i+1):
#             print("*",end=" ")
#         print()
# elif new ==False:
#     for i in range(one,0,-1):
#         for z in range(1,i+1):
#             print("*", end="")
#         print()

# rows = int(input('Enter the number of rows you want for the stairs : '))
# print()
# stairs = bool(int(input("Enter 1 of regular stairs and 0 for inverted stairs : ")))
# print()
# if stairs:
#     for i in range(1, rows + 1):
#         print('* ' * i)
# elif not stairs:
#     for i in range(rows, 0, -1):
#         print('* ' * i)
#
rows = int(input("Enter the number of rows\n"))
stairs = int(input("Enter 1 or 0\n"))
if stairs==1:
    for i in range(1,rows +1):
        print('*' *i)
elif stairs==0:
    for i in range(rows,0,-1):
        print('*'*i)
else:
    print("please enter valid key")