#OOPs 2 part 
# kal ham pada tha kis tha class banya ajata hai or object likha jata hai or uska methods 
 #del keyword 

class student :
    def __init__(self,name ):
        self.name =name 

s1 = student ("Nehal ")
print (s1.name )

#del s1.name 
#print (s1.name )

# private 
class  Account :
    def __init__(self,acc_no , acc_passw):
        self.acc_no= acc_no
        self.acc_passw=acc_passw
        print (" NEHAL Account Deatils ")


acc1 = Account (56789,5689)
print (acc1.acc_no)
#print (acc1.__acc_passw) # it go into private

# Inheritance 

class car:
    @staticmethod 
    def start():
        print ("Car started ")

    @staticmethod 
    def stop():
        print ("Car stoped ")

class Toyota_car (car):
    def __init__(self,name ):
        self.name = name 

car1 = Toyota_car ("fortuner" )
car2 = Toyota_car ("j Class ")

print (car1.start())
print (car2.stop())

# Inheritance Types (single ,multileval , multiple )

# single inheritance (last example )

# Multi - level - Inheritance 

class car:
    @staticmethod 
    def start():
        print ("Car started ")

    @staticmethod 
    def stop():
        print ("Car stoped ")

class Toyota_car (car):
    def __init__(self,type  ):
        self.type  = type 

class fortuner ( Toyota_car ):
    def __init__(self ,brand ):
        self.brand =brand 

car1 = fortuner ("Disel ")
print (car1.brand )


# Multiple InheritANCE 
class A:
    varA = "Welcome to class A "
class b:
    varb = "Welcome to class b"
class c  (A ,b):
    varc = "Welcome to class c "

c1 =c()
print (c1 .varc)
print (c1.varb)
print (c1.varA)

# Super method
class car:
    def __init__(self,type ):
        self.type = type  
    
    @staticmethod 
    def start():
        print ("car start")
    
    @staticmethod 
    def stop():
        print ("car stopped ")
    
class toyotacar (car):
    def __init__(self,name,type  ):
        self.name = name 
        super().__init__(type ) # spuer method 
        super().start ()
        super().stop()
car1 = toyotacar ("supra ", "petrol ")
print (car1.name ,car1.type )

#Class method  
class person:
    name = "anonymous "

   # def changename (self,name ):
        #person .name =name 

    @classmethod #class method use 
    def changename (cls,name ):
        cls.name =name 
    

p1 = person()
p1.changename ("adtiya ")
print (p1.name )
print (p1.name )#doesn't chane name 
print (person .name )# change the name 


#property decorator 

class student :
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
    @property
    def percentage (self):
        return str ((self.phy+self.chem+ self.math )/3 ) +"%"


student1 = student (90,78,98)
print (student1.percentage )

student1.math = 55
print (student1.percentage )

#Polymorphism 

# for add (a+b )   is use __add__
# for sub (a-b) is use __sub__
# for div (a/b ) is use __truediv__
# for multiply (a*b ) is use __mul__
# or bhi bhot hai 
