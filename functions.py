def fun1(a,b):
    '''This is a average functions'''
    average = (a+b)/2
    return (average)
v=fun1(int(input("Please enter frist no\n")),int(input("Please enter Second no\n")))
print(v)
print(fun1.__doc__)