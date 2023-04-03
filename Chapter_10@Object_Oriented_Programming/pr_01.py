class Employee:
    company = "Microsoft"
    def __init__ (self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def getInfo(self):
        print(f"The programmer named {self.name} is working in {self.company} and his age is {self.age}. His salary is {self.salary}")

ram = Employee("Ram", 28, 25000)
ram.getInfo()
sham = Employee("Sham", 32, 30000)
sham.getInfo()

