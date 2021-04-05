# def function_name_print(a, b, c, d, e):
#     print(a, b, c, d, e)

# def funargs(normal, *argsrohan, **kwargsbala):
#     print(normal)
#     for item in argsrohan:
#         print(item)
#     print("\nNow I would Like to introduce some of our heroes")
#     for key, value in kwargsbala.items():
#         print(f"{key} is a {value}")
#
#
# # function_name_print("Harry", "Rohan", "Skillf", "Hammad", "Shivam")
#
# har = ["Harry", "Rohan", "Skillf", "Hammad",
#        "Shivam", "The programmer"]
# normal = "I am a normal Argument and the students are:"
# kw = {"Rohan": "Monitor", "Harry": "Fitness Instructor",
#       "The Programmer": "Coordinator", "Shivam": "Cook"}
# funargs(normal, *har, **kw)
#

def funarg(normal,*har,**har1):
    print(normal)
    print(har[0],har[1])
    for key,value in har1.items():
        print(f"{key} is {value}")


normal= "Mrinmoy is a good boy"
har="Mrinmoy","Manika","Ratan"
har1 ={"Harry":"Programmer","Larry": "Codder", "Perry":"Scientist"}
funarg(normal, *har,**har1)