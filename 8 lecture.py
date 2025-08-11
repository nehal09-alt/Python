# OOPS = object oriented programing system
#object bana sa phale hame uskal  class bana par ta hia 
#clas = "blue print " for creating objects 

class student :
    name = "Karan "
    name2 ="nehal "

s1 = student ()
print (s1.name )

s2 = student()
print (s2.name2 )

#2 
class car:
    color = "                Black "

car1 = car()
print (car1.color )

# __init__ function ( constructor )
  
class student :
    name = "Karan "
    name2= "Nehal "
    def __init__(self):
        print ("adding new name in database ")
    

s1 = student ()
print (s1.name )
s2 = student ()
print (s2.name2 )

#2 k0 karna ka naya tarika 
#parameterzied constructor :
class student :
    school= "ham to mila"
    def __init__(self,fullname,marks , ):
        self.name=fullname 
        self.marks=marks
        
        print ("adding new name in database ")
    

s1 = student ("karan ",97)
print (s1.name,s1.marks, s1.school  )
s2 = student ("nehal",90)
print (s2.name , s2.marks,s2.school)

# attributes (1 . class, 2 . Instance  )
# class means sab same ho # instance sab value alag ho


# Methods 
# methods are function that belong to object 

#craeting class ....

class car:
    def __init__(self,name , Model):
        self.name=name
        self.Model=Model 
        print ("CAR bluePrint ")

#creating object ...

car1 = car("Thar ", "v24")
print (car1.name ,car1.Model)

# static Methods 
#            @staticmethod
# main pillar of oops >>>>>
#(Abstraction .....)
#(Encapsulation  .....)
#(Inheritance  ....)
#(Polymorphism  ....)


#1 Abstracion 

class car:
    def __init__ (self):
        self.accelartor= False
        self.brake=False 
        self .clutch =False 
    def start (self):
        self.clutch=True 
        self.accelartor=True 
        print ("Car started ....")

car1= car()
car1.start()


#2 Encaapsulation 
# data + function = capsulation == Encapsulation 
# we did it i upper  example .



 