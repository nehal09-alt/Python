# questionn


#define a circle class to create a circle with radius r usint the constructor .

class circle :
    
    def __init__(self,radius ):
        self.radius =radius 
    def area (self ):
        return 3.14 * self.radius **2
    def parimetere (self):
        return 2 *3.14 *self.radius 
    
    
circle1 = circle(14)
print (circle1.area() ) 
print (circle1 .parimetere())


# 2 
class Employe :
    def __init__(self,role  , depart,salary ):
        self.role =role 
        self.depart=depart
        self.salary=salary
    def showdetails(self):
        print ("role = ",self.role )
        print ("depart=",self.depart)
        print ("salary =",self.salary)

class engineer(Employe ) :
    def __init__(self,name ,age ):
        self.name =name 
        self.age =age 
        super().__init__("manager ", "IT", 2000000)

eng1 = engineer("nehal ",25)
eng1.showdetails()