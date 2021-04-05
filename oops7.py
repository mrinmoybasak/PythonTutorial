
class Employee:
    no_of_leaves = 8
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole
    def printdetails(self):
        return f"Name is {self.name}.Salary is {self.salary}. and role is {self.role}"
    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_str(cls,string):
        # params = string.split("/")
        # return cls(params[0],params[1],params[2])
        #   or
        return cls(*string.split("/"))
    @staticmethod
    def printname(string):
        print("This is my name " + string)
class Programmer(Employee):
    def __init__(self,aname,asalary,arole, lan):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.lan = lan




    def printprog(self):
        return f"The Programmer's Name is {self.name}.Salary is {self.salary}. and role is {self.role}. The languages are {self.lan}"



harry = Employee("Harry",255,"Instructor")
rohan = Employee("Rohan",455,"Student")
# karan = Employee.from_str("Karan/480/Student")

shubham = Programmer("Shubham", 555, "Programmer",["Python"])
karan = Programmer("Karan", 777, "Programmer", ["Python","cpp"])
print(karan.printprog())

# karan.printname("Mrinmoy")
# rohan.change_leaves(34)
# print(harry.no_of_leaves)