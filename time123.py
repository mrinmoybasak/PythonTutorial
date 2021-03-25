import time
initial = time.time()
k=0
# while(k<45):
#     print("This is Mrinmoy2")
#     k+=1
#     print("While loop run in", time.time() - initial, "Seconds")
# initial2 = time.time()
# # for i in range(45):
#     print("This is Mrinmoy")
#     print("For loop run in", time.time() - initial2, "Seconds")

# while k<10:
#     name = input("Enter Your name or roll no-\n")
#     if name.isalpha():
#         print("Your Name is ", name)
#         k+=1
#         print("You have left",(10-k),"Times" )
#         print ("Currennt Date & Time is",time.asctime(time.localtime(time.time())))
#
#     elif name.isnumeric():
#         print("Your Roll no is", name)
#         k+=1
#         print("You have left", (10 - k), "Times")
#         print("Currennt Date & Time is", time.asctime(time.localtime(time.time())))
#     else:
#         print("Please valid input")
n = [ ["Harry", 1], ["Larry", 2],
        ["Carry", 6], ["Marie", 250]]
number = dict(n)
for item, num in number.items():

    print(item,number(1))







