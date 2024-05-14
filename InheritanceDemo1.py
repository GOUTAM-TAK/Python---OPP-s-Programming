class Employee:

    def __init__(self, name, salary) -> None:
        self.name = name
        self.salary = salary
    
    def employee_details(self):
        print(f"name : {self.name} salary : {self.salary}")


class Programmer(Employee):

    def __init__(self, name, salary, programming_language) -> None:
        super().__init__(name, salary)    #Employee.__init__(self, name, salary)
        self.programing_language  = programming_language


my_programmer = Programmer("Vinay", 25000, "C#")

print(f" name : {my_programmer.name} salary : {my_programmer.salary} programing_language : {my_programmer.programing_language}")
my_programmer.employee_details()   #base class method inherit
     
class Data_Engineer(Programmer):
    pass

my_eng = Data_Engineer("Rajesh", 25000, "Java")
my_eng.employee_details()