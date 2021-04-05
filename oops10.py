
class Employee:
    no_of_leaves = 8
    _pro = 12
    __pri = 15

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
class Player:
    no_of_games = 4
    def __init__(self,name,game):
        self.name = name
        self.game = game
    def printdetails(self):
        return f"Name is {self.name}.Game is {self.game}"
class CoolProgrammer(Employee,Player):
    languages = "c++"
    def printlaguages(self):
        print (self.languages)




harry = Employee("Harry",255,"Instructor")
rohan = Employee("Rohan",455,"Student")

shubham = Player("Subham",["Criket"])
karan = CoolProgrammer("Karan",8999,"CoolProgrammer")
# det = karan.printdetails()
# det=karan.printdetails()
# print(det)
print(harry._Employee__pri)
