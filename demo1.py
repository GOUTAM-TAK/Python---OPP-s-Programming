class Demo:
    
    def __init__(self) -> None:
        self.items = []

obj1 = Demo()
print(obj1)

#one Argument

class Circle:
    def __init__(self, radius):
        self.radius = radius

circle_obj = Circle(10.0)
print(circle_obj)

#Multiple Argument

class Rectangle:
    def __init__(self, height, width) -> None:
        self.height = height
        self.width = width

react_obj1 = Rectangle(5.6, 3.7)
react_obj2 = Rectangle("hello",5.0)        #here for obj2 height has string data type
print(react_obj1)
print(react_obj1.height)
print(react_obj2.height)

#None - it's object used to declare null variable

print(isinstance(None, object))      #True
print(type(None))     #class NoneType

#Acess instance attribute

print(react_obj1.height)

#Default value = don't use spaces around = sign during default value asign, Default argument must be in rigth side in parameter list

class Demo3:
    def __init__(self, range=5) -> None:
        self.range=range
    
obj_demo3 = Demo3(2)
print(obj_demo3.range)

obj2_demo3 = Demo3()
print(obj2_demo3.range)

#iteration over list
objects = [obj_demo3, obj2_demo3]
for obj in objects:
    print(f"range : {obj.range}")


#Class Attributes = define before init method, they belong to class and share b/w all instances
class Dog:
    spicies = "C. Lemun"
    dog_id = 1
    def __init__(self, color, breed) -> None:
        self.id = Dog.dog_id
        self.color = color
        self.breed = breed

        Dog.dog_id += 1      #class attribute access by class name

dog1 = Dog("white", "german")

#Dog.dog_id = 5
print(f"class attr : {dog1.dog_id}")
Dog.dog_id=5
dog2 = Dog("Brown", "Italy")
print(f"id : {dog1.id} species : {dog1.spicies} color : {dog1.color} breed : {dog1.breed}")
print(f"id : {dog2.id} species : {dog2.spicies} color : {dog2.color} breed : {dog2.breed}")


del dog1.breed
print(f"species : {dog1.spicies} color : {dog1.color}")