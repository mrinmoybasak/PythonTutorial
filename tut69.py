class Employee:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname} @mbwealth.in"

    def explain(self):
        return f"This emplioyee is {self.fname} {self.lname}"
    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email is not set"
        return f"{self.fname}.{self.lname} @mbwealth.in"
    @email.setter
    def email(self,string):
        print("Setting Now..")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname= None
        self.lname= None

mrinmoy = Employee("Mrinmoy", "Basak")
manika = Employee("manika", "Majumder")

# print(mrinmoy.email)

mrinmoy.fname = "Ratan"

# print(mrinmoy.email)
mrinmoy.email = "this.that@mbwealth.in"
# print(mrinmoy.email)
del mrinmoy.email
print(mrinmoy.email)
mrinmoy.email = "Harry.Perry@mbwealth.in"
print(mrinmoy.email)