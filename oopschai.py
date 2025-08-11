class car :
    total_car = 0 
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        car.total_car+=1 
    def full_name(self):
        return f"{self.brand} {self.model}"
    
my_car = car("Hundai", "TYpe R")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())
my_car1 = car("jeep", "4x4")
print(my_car1.brand)
print(my_car1.full_name())
print(car.total_car)

#calculate area of circle 
import math
class area :
    def __init__(self , radius):
        self.radius = radius
    def ar(self):
        return math.pi *self.radius **2 
    
    
my_area= area(2)
print(my_area.ar())

#inheritance   father-> to son 

class Electric_car(car):
    def __init__(self , brand ,model , battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
    def size (self):
        return f"{self.model} {self.brand} {self.battery_size}"
    
my_car2 = Electric_car("Tesla" ,"CyberTruck" , "56kwh")
print(my_car2.model)
print(my_car2.full_name())
print(my_car2.size())

#example of Inheitence 

class Nehal:
    def __init__(self , name , age , year):
        self.name = name 
        self.age = age
        self.year = year
    def xxx(self):
        return f"{self.name} {self.age} {self.year}"

student = Nehal("Md Nehal KHurshid", 19 , 2005 )
print(student.xxx())


class md(Nehal):
    def __init__(self, name , age , year , education):
        super().__init__(name , age , year)
        self.education = education

student1= md("Md Jishan Khurshid", 21 , 2003 , 10 )
print(student1.education)

#encapsulation - operate data in (private)

class minster :
    def __init__(self , name , title):
        self.__name = name 
        self.title = title 
    def get_name(self):
        return self.__name  + ","
    def full (self):
        return f"{self.__name} {self.title}"
    
my_minster = minster("Nehal" , "Prime Minster")
#print(my_minster.__name)  # so here if we used (__)it get private and give attribute error 
print(my_minster.get_name())
print(my_minster.full())

# example of encapsulation 
class  Account :
    def __init__(self,acc_no , acc_passw):
        self.acc_no= acc_no
        self.acc_passw=acc_passw
        print (" NEHAL Account Deatils ")


acc1 = Account (56789,5689)
print (acc1.acc_no)
print(acc1.acc_passw)
#print(acc1.__acc_passw)# after addinng(__)it gets private 

# polymorphism (take many roop )


class vechile :
    def __init__(self , company , models):
        self.company = company
        self.models =models
        
    def fuel_type (self):
        return "petrol or Deisel "

class electric(vechile):
    def __init__(self , company , models , ):
        super().__init__(company , models)
        
    
    def luuf(self):
        return f"{self.company} {self.fuel_type} {self.electric_car}"
    
    def fuel_type (self):
        return "Electric_Charge "


my_car3 = electric("Tesla" , "XT4" )
print(my_car3.fuel_type())

my_car4= vechile("Tata", "Thar" )
print(my_car4.fuel_type())


#example of polymorphism 

#title change :

class name:
    def __init__(self,Name):
        self.Name= Name 
        print("My name is : ")
    def title (self):
        return "khurshid Ansari"
    
class naam (name):
    def __init__(self , name , age ):
        super().__init__(name)
        self.age= age
    def title (self):
        return "Khurshid"
    
my_name= naam("Md Nehal", 19)
print(my_name.title())

my_name1= name ("Md Nehal")
print(my_name1.title())

#class variables (kitna total object ha uska counting)
# i did this in code 1 go and checkout
#use only 


#totoal_car = 0 
#car.total_car+=1

#print(car.total_car)

#Static Method --decoraters 
#@static method belong to class rather than object
#jab static method lag ga to self use nahi hoga 



class hero :
    def __init__(self, company , models ):
        self.company= company
        self.models = models

    @staticmethod
    def general_description():
        return f"car is mean of transprt"


hero("Hundai","Thar")
#print(vechile.company )
#print(vechile.models)
print(hero.general_description())


#@property --decoraters 
# use for private (acces nahi dena dusro ko change karna ka )
class car :
    def __init__(self , name , model):
        self.name = name 
        self.__model =model 
    @property
    def model(self):
        return self.__model

my_car5 = car("Maruthi", "lexus ")
print(my_car5.model)

#class inheritance ans isinstance()
#isinstance prove karta hai ki wo class ka hai ya nhai (true or false mai)

class car:
    def __init__(self , brand ,model):
        self.brand = brand
        self.model = model
class electric_car(car):
    def __init__(self , brand ,model , type):
        super().__init__(brand , model)
        self.type= type

my_car6=electric_car("tesla", "xxx", "Battery")
print(my_car6.type)
print(isinstance(my_car6 ,electric_car))
print(isinstance (my_car6, car))


#multiple inheritance 
#hota ak sa jada class connect kar lata hai

#class battery :
 #   def battery_info(self):
  #      return "this is battery car"

#class engine :
    #def engine_car (self):
       # return "this eengine car"

#class electric(battery , engine ):
  #  pass

#my_new_car = electric("Tesla" , "model S ")
#print(my_new_car.battery_info())
#print(my_new_car.engine_car())


#example :  
class Fruits:
    def __init__(self, name, taste):
        self.name = name
        self.taste = taste

    def get(self):
        return f"{self.name}, {self.taste}"

class Ripe(Fruits):
    def __init__(self, name, taste, owner):
        super().__init__(name, taste)
        self.owner = owner

    def fulls(self):
        a = int(input("Enter your number: "))
        if 0 <= a <= 10:
            print("ok")
        else:
            print("BAdAss Ravikumar")

class Unripe(Ripe):
    def __init__(self, name, taste, owner, things):
        super().__init__(name, taste, owner)
        self.things = things

    def gpu(self):
        return f"{self.name}, {self.taste}, {self.owner}, {self.things}"

my_fruits = Unripe("Banana", "Sweet and glimpse", "Raju", "Good to health")
print(my_fruits.gpu())
print(my_fruits.fulls())
print(my_fruits.get())

































