#Public Non-Public attribute
#1)by naming convention '_'    2)Name mangling

#Getters and Setters -   def get_<attribute>(self):       setter-  def set_<attribute>(self, new_value):
class Demo:

    def __init__(self, name, color, size) -> None:
        self.name = name
        self._size = size    #By naming convention
        self.__color = color #By Name Mangling - now attribute name changed automatically into '_Demo__color'
 
    def set_size(self, new_size):
        if new_size > 5.0 and isinstance(new_size, float):     #float or int   5.8 < new_size < 30.6
            self._size=new_size
        else:
            print("size must be greater than 5")
     
    def set_color(self, new_color):
        if isinstance(new_color, str) and new_color.isalpha():
            self.__color=new_color

        else:
            print("enter valid color value")


    def get_size(self):
        return self._size
    
    def get_color(self):
        return self.__color
    
    color = property( get_color, set_color)
    size = property( get_size, set_size)

obj1 = Demo("Vinay", "White", "5fit")
print(obj1._size)    #compiler shows only warning for don't use outside class

#print(obj1.__color)     #error bocz of name mangling
print(obj1._Demo__color)   #now by this way we can access

print("by getter values are : ") 
print(f"color : {obj1.get_color()}   size : {obj1.get_size()}")

#after setter
print("enter new values for color and size")

obj1.set_color("white123")
obj1.set_color("white")

obj1.set_size(3.6)
obj1.set_size(7.0)

print("by getter new values are : ") 
print(f"color : {obj1.get_color()}   size : {obj1.get_size()}")

print("update by property : ")
obj1.size=7.5     #automatically setter called
obj1.color="Black"  

print("by property new values are : ") 
print(f"color : {obj1.color}   size : {obj1.size}")    #automatically getter called


#Property Decorator -  @property

class Demo2:

    def __init__(self, name, age=18) -> None:
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new_age):
        if isinstance(new_age, int) and 18 <= new_age <=35:
            self._age = new_age

        else:
            print("enter valid age")


demo2_obj1 = Demo2("Rahul", 27)

print(f"name is : {demo2_obj1.name}  age : {demo2_obj1.age}")

print("after updating :")
demo2_obj1.age = 33
print(f"name is : {demo2_obj1.name}  age : {demo2_obj1.age}")


