class Computer:
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Config is", self.cpu,self.ram)


com1 = Computer("i5","8gb")
com2 = Computer("i7","16gb")

com1.config()
com2.config()

print(f"Computer 1 CPU is {com1.cpu} and Computer 1 Ram is {com1.ram}")
print(f"Computer 2 CPU is {com2.cpu} and Computer 2 Ram is {com2.ram}")
