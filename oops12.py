class A: #(name=father)
    classvar1 = "I am a class variable in class A" #print 4th father class if not super
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "instance var in class A"  #print 3rd father instance if not super
        self.special = "Special"
class B(A): #(name =Son)  Rule of print variable if not super
    classvar1 = "I am in Class B"  #print 2nd own class if not super
    def __init__(self):
        super().__init__()  # to use father's attribute and method now can use variable name= spacial
        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "instance var in class B"    #print 1st own instance if not super



a = A()
b = B()

print(b.special, b.var1,b.classvar1)