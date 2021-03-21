# x= 10
# def mrinmoy():
#     global x
#     x =88
#     print(x)
# mrinmoy()
x=89
def mrinmoy():
    x=20
    def manika():
        global x
        x=88
        print("before calling manika()",x )
    manika()

    print("after calling manika()", x)
mrinmoy()
print(x)


