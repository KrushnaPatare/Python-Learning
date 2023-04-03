class School: #variables + Methods
    name="RHS"
    def __init__ (self): #Constructor --> code in constructor run everytime when we run a programme, without calling it 
        print("The programme is started.")
        
    def subjects(self):
        print("English,Maths,Science,History,Marathi")

    @staticmethod #when you do not wont to give argument or it is not needed.
    def work():
        print("All student have to do homework.")

Residential = School()  #Object --> Residential
n=Residential.name      #class variable
print(n)
print(Residential.name)
m=Residential.name = "Firodiya" #instance variable  --> because variable value is changed.
Residential.new="I am totally new variavle."
print(m)
print(Residential.name)
print(Residential.new)

Residential.work()