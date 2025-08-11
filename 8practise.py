#craete student class take name &marks of three students 
#as argument in constructor .Then create  method to Print the  average 


class student :
    def __init__(self,name ,marks ):

        self.name =name 
        self.marks=marks 
    
        print ("adding student name and marks ")
    def average (self ):
        sum=0
        for val  in self.marks :
            sum +=val
            print (self.name ,sum/3)

        

s1 =student ("Nehal ",[90,80,89])

s1.average ()

#2 Create account class with 2 attributes - balance &acount no. 
# create methods for debit ,credit & printig the balance .



class Account :
    def __init__(self, Balnce ,Accountnum):
        self.Balance =Balnce 
        self.Account = Accountnum
        print ("Adding Account Detailss.. ")
       
#debit method
    def debit (self,amount ):
        self .Balance -=amount 
        print ("amount Debit ",amount , "was debit ") 
        # credit method 
    def  credit (self, amount ):
        self.Balance +=amount 
        print ("amount credit ",amount,"was Credit ")
        print ("Total balance ",self.get_Balance ())
    def get_Balance (self ):
        return self.Balance 

acc1 =Account (100, 5689)
acc1.debit (10)
acc1.credit (2000)
acc1.debit (10)
acc1 .credit (110)

