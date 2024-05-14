class Demo3:

    def __init__(self, name, age) -> None:
        self._name = name
        self.__age = age
        self._hobies = []
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and new_name.isalpha:
            self._name = new_name

        else:
            print("give valid name")

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, new_age):
        if isinstance(new_age, int) and new_age >= 18:
            self.__age = new_age

        else:
            print("enter valid age")
    
    @age.deleter
    def age(self):
        del self.__age

    def add_hobbies(self, new_hobby):
        if new_hobby not in self._hobies:
            self._hobies.append(new_hobby)

        else:
            print("already registered ")
    
    @property
    def hobies(self):
        return self._hobies
    
obj1 = Demo3("Shyam", 27)
obj1.add_hobbies("reading")    #call method
#alternative way to call
Demo3.add_hobbies(obj1, "singing")

print(obj1.hobies)
print(f"name : {obj1.name} age : {obj1.age} hobbies : {obj1.hobies}")

#del obj1.age
#print(f"name : {obj1.name} age : {obj1.age} hobbies : {obj1._hobies}")


